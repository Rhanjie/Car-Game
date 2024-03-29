from tkinter import RIGHT, LEFT, Canvas

from car import Car
from direction import Direction
from object import Object


class Player(Car):
    def __init__(self, x: int, y: int, color: str, velocity: float):
        Object.__init__(self, x, y, color)

        self.vertical_offset = y
        self.start_x = x

        self.y = 0
        self.velocity = 0
        self.current_velocity = 0
        self.vertical_distance = 0
        self.horizontal_step = 10

        self.road_left_side = 0
        self.road_right_side = 0

        self.start(velocity)

    def start(self, max_velocity: float):
        if max_velocity is not None:
            self.velocity = float(max_velocity)

        self.x = self.start_x
        self.current_velocity = 0
        self.y = -self.vertical_offset
        self.vertical_distance = self.y + self.vertical_offset

    def register_road_size(self, road_left_side: float, road_right_side: float):
        self.road_left_side = road_left_side
        self.road_right_side = road_right_side

    def change_direction(self, direction: Direction):
        if direction == RIGHT and self.x + self.width < self.road_right_side:
            self.x += self.horizontal_step

        if direction == LEFT and self.x - 10 > self.road_left_side:
            self.x -= self.horizontal_step



    def update(self, current_y: int):
        Car.update(self, current_y)

        self.vertical_distance = self.y + self.vertical_offset

    def draw(self, canvas: Canvas, current_y: int):
        canvas.create_rectangle(
            self.x, self.vertical_offset - self.height, self.x + self.width, self.vertical_offset, fill=self.color)
