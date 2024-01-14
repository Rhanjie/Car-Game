from tkinter import RIGHT, LEFT, Canvas

from car import Car
from direction import Direction
from object import Object


class Player(Car):
    def __init__(self, x: int, y: int, color: str, velocity: float):
        Object.__init__(self, x, y, color)

        self.velocity = velocity
        self.current_velocity = 0

        self.vertical_offset = y
        self.y = -self.vertical_offset

        self.vertical_distance = self.y + self.vertical_offset

    def change_direction(self, direction: Direction):
        if direction == RIGHT:
            self.x += 10

        elif direction == LEFT:
            self.x -= 10

    def update(self, current_y: int):
        Car.update(self, current_y)

        self.vertical_distance = self.y + self.vertical_offset

    def draw(self, canvas: Canvas, current_y: int):
        canvas.create_rectangle(
            self.x, self.vertical_offset - self.height, self.x + self.width, self.vertical_offset, fill=self.color)
