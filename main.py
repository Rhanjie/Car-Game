from abc import ABC, abstractmethod
from tkinter import *
from enum import Enum
import random


class Object(ABC):
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

        self.width = 20
        self.height = 40

    @abstractmethod
    def update(self, current_y: int):
        pass

    @abstractmethod
    def draw(self, canvas: Canvas, current_y: int):
        pass

    def ready_to_delete(self, current_y: int) -> bool:
        return current_y - self.y > 800 # 100 - 150


class Line(Object):
    def __init__(self, x: int, y: int, color: str):
        Object.__init__(self, x, y, color)

        self.width = 5
        self.height = 60

    def update(self, current_y: int):
        pass

    def draw(self, canvas: Canvas, current_y: int):
        y_screen = current_y - self.y

        square = canvas.create_rectangle(
            self.x, y_screen, self.x + self.width, y_screen + self.height, fill=self.color)


class Obstacle(Object):
    def __init__(self, x: int, y: int, color: str):
        Object.__init__(self, x, y, color)

    def update(self, current_y: int):
        pass

    def draw(self, canvas: Canvas, current_y: int):
        y_screen = current_y - self.y

        square = canvas.create_rectangle(
            self.x, y_screen, self.x + self.width, y_screen + self.height, fill=self.color)


class Car(Object):
    def __init__(self, x: int, y: int, color: str, velocity: float):
        Object.__init__(self, x, y, color)

        self.velocity = velocity
        self.current_velocity = 0

    def update(self, current_y: int):
        if self.current_velocity < self.velocity:
            self.current_velocity += 1

        self.y += (self.current_velocity * 0.02)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2


class Player(Car):
    def __init__(self, x: int, y: int, color: str, velocity: float, vertical_offset: int):
        Object.__init__(self, x, y, color)

        self.velocity = velocity
        self.current_velocity = 0

        self.vertical_offset = vertical_offset

    def change_direction(self, direction: Direction):
        if direction == RIGHT:
            self.x += 10

        elif direction == LEFT:
            self.x -= 10

    def draw(self, canvas: Canvas, current_y: int):
        square = canvas.create_rectangle(
            self.x, self.vertical_offset - self.height, self.x + self.width, self.vertical_offset, fill=self.color)


class Terrain:
    def __init__(self, lines_color: str, road_width: int, screen_width: int, screen_height: int):
        self.lines_color = lines_color
        self.background_items = []
        self.obstacles = []

        self.road_width = road_width
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.total_obstacles_spawned = 0
        self.total_centered_lines_spawned = -4

        self.spawn_road_cropped_line(-600)
        self.spawn_road_cropped_line(-450)
        self.spawn_road_cropped_line(-300)
        self.spawn_road_cropped_line(-150)

    def update(self, current_y: int):
        self.background_items[:] = [item for item in self.background_items if not item.ready_to_delete(current_y)]
        self.obstacles[:] = [obstacle for obstacle in self.obstacles if not obstacle.ready_to_delete(current_y)]

        self.spawn_obstacle(current_y)
        self.spawn_road_cropped_line(current_y)

    def draw(self, canvas: Canvas, current_y: int):
        for item in self.background_items:
            item.draw(canvas, current_y)

        for obstacle in self.obstacles:
            obstacle.draw(canvas, current_y)

        self.draw_road_side_lines(canvas)

    def spawn_obstacle(self, current_y: int):
        should_spawn = (current_y / 200 > self.total_obstacles_spawned)
        if not should_spawn:
            return

        offset = int((self.screen_width - self.road_width) / 2)

        position_x = random.randint(offset, self.screen_width - offset)
        self.obstacles.append(Obstacle(position_x, current_y, "#FFFF00"))
        self.total_obstacles_spawned += 1

    def spawn_road_cropped_line(self, current_y: int):
        should_spawn = (current_y / 150 > self.total_centered_lines_spawned)
        if not should_spawn:
            return

        position_x = self.screen_width / 2
        self.obstacles.append(Line(position_x, current_y, self.lines_color))
        self.total_centered_lines_spawned += 1

    def draw_road_side_lines(self, canvas: Canvas):
        offset = int((self.screen_width - self.road_width) / 2) - 30
        side_line_x1 = offset
        side_line_x2 = self.screen_width - offset

        canvas.create_rectangle(
            side_line_x1, 0, side_line_x1 + 5, self.screen_height, fill=self.lines_color)

        canvas.create_rectangle(
            side_line_x2, 0, side_line_x2 + 5, self.screen_height, fill=self.lines_color)


class GameManager:
    def __init__(self, width: int, height: int, color: str):
        self.window = Tk()
        self.window.title("Car Game - Python GUI Project")

        self.label = Label(self.window, text="", font=('consolas', 20))
        self.label.pack()

        self.canvas = Canvas(self.window, bg=color, height=height, width=width)
        self.canvas.pack()

        self.terrain = Terrain("#ffffff", 300, width, height)

        self.window.update()

    def main_loop(self, player: Player):
        self.init_events(player)

        self.next_turn(player)

        self.window.mainloop()

    def init_events(self, player: Player):
        self.window.bind('<Left>', lambda event: player.change_direction(LEFT))
        self.window.bind('<Right>', lambda event: player.change_direction(RIGHT))

    def next_turn(self, player: Player):
        self.update(player)
        self.draw(player)

    def update(self, player: Player):
        self.terrain.update(player.y)
        player.update(0)

    def draw(self, player: Player):
        self.canvas.delete('all')

        self.label.config(text="Points:{} - {}".format(player.y, player.current_velocity))

        self.terrain.draw(self.canvas, player.y)
        player.draw(self.canvas, 0)

        self.window.after(16, self.next_turn, player)


if __name__ == '__main__':
    width = 800
    height = 600

    game_manager = GameManager(800, 600, "#000000")
    player = Player(int(width / 2), 0, "#00FF00", 300, 500)

    game_manager.main_loop(player)
