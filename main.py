from tkinter import *
from enum import Enum


class Direction(Enum):
    RIGHT = 1
    LEFT = 2


class Car:
    def __init__(self, velocity: float, color: str, x: int, y: int):
        self.velocity = velocity
        self.color = color

        self.current_velocity = 0
        self.x = x
        self.y = x

        self.width = 20
        self.height = 40

    def display(self, canvas: Canvas):
        square = canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)

        if self.current_velocity < self.velocity:
            self.current_velocity += 1

        self.y += 1


class Player(Car):
    def change_direction(self, direction: Direction):
        if direction == RIGHT:
            self.x += 20

        elif direction == LEFT:
            self.x -= 20


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

        player.display(self.canvas)

        self.window.after(200, self.next_turn, player)


class Terrain:
    def __init__(self, lines_color: str):
        obstacles = []

    def update(self, current_y, int):
        # remove obstacles from list if y < player.y

        # randomize spawn the random obstacle in random x position

        pass

    def draw(self, current_y: int):
        # draw obstancles from list

        # draw centered lines

        # draw side lines

        pass


class Obstacle:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y


if __name__ == '__main__':
    game_manager = GameManager(800, 600, "#000000")
    player = Player(100, "#00FF00", 400, 100)

    game_manager.main_loop(player)
