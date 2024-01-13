from abc import ABC, abstractmethod
from tkinter import *
from enum import Enum
import random


class Object(ABC):
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = x
        self.color = color

        self.width = 20
        self.height = 40

    @abstractmethod
    def update(self, canvas: Canvas, current_y: int):
        pass

    @abstractmethod
    def draw(self, canvas: Canvas, current_y: int):
        pass

    def ready_to_delete(self, current_y: int) -> bool:
        return self.y < current_y


class Obstacle(Object):
    def __init__(self, x: int, y: int, color: str):
        Object.__init__(self, x, y, color)

    def update(self, canvas: Canvas, current_y: int):
        pass

    def draw(self, canvas: Canvas, current_y: int):
        y_screen = self.y - current_y

        square = canvas.create_rectangle(
            self.x, y_screen, self.x + self.width, y_screen + self.height, fill=self.color)


class Car(Object):
    def __init__(self, x: int, y: int, color: str, velocity: float):
        Object.__init__(self, x, y, color)

        self.velocity = velocity
        self.current_velocity = 0

    def update(self, canvas: Canvas, current_y: int):
        if self.current_velocity < self.velocity:
            self.current_velocity += 1

        self.y += 1

    def draw(self, canvas: Canvas, current_y: int):
        square = canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2


class Player(Car):
    def change_direction(self, direction: Direction):
        if direction == RIGHT:
            self.x += 20

        elif direction == LEFT:
            self.x -= 20


class Terrain:
    def __init__(self, lines_color: str, screen_width: int, screen_height: int):
        self.lines_color = lines_color
        self.obstacles = []

        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, current_y: int):
        self.obstacles[:] = [obstacle for obstacle in self.obstacles if not obstacle.ready_to_delete(current_y)]

        chance = random.randint(0, 100)
        if chance > 20:
            return

        position_x = random.randint(0, self.screen_width)
        self.obstacles.append(Obstacle(position_x, current_y + self.screen_height, "FFFF00"))

    def draw(self, canvas: Canvas, current_y: int):
        for obstacle in self.obstacles:
            obstacle.draw(canvas, current_y)

        # draw centered lines

        # draw side lines

        pass


class GameManager:
    def __init__(self, width: int, height: int, color: str):
        self.window = Tk()
        self.window.title("Car Game - Python GUI Project")

        self.label = Label(self.window, text="", font=('consolas', 20))
        self.label.pack()

        self.canvas = Canvas(self.window, bg=color, height=height, width=width)
        self.canvas.pack()

        self.window.update()

    def main_loop(self, player: Player):
        self.init_events(player)

        self.next_turn(player)

        self.window.mainloop()

    def init_events(self, player: Player):
        self.window.bind('<Left>', lambda event: player.change_direction(LEFT))
        self.window.bind('<Right>', lambda event: player.change_direction(RIGHT))

    def next_turn(self, player: Player):
        self.canvas.delete('all')

        self.label.config(text="Points:{}/{}".format(player.current_velocity, player.velocity))

        player.draw(self.canvas, 0)

        self.window.after(200, self.next_turn, player)


if __name__ == '__main__':
    width = 800

    game_manager = GameManager(800, 600, "#000000")
    player = Player(int(width / 2), 0, "#00FF00", 200)

    game_manager.main_loop(player)
