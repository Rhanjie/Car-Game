from tkinter import RIGHT, LEFT, Canvas

from car import Car
from direction import Direction
from object import Object


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
