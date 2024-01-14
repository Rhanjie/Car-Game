from object import Object
from obstacle import Obstacle


class Car(Obstacle):
    def __init__(self, x: int, y: int, color: str, velocity: float):
        Object.__init__(self, x, y, color)

        self.velocity = velocity
        self.current_velocity = 0

    def update(self, current_y: int):
        if self.current_velocity < self.velocity:
            self.current_velocity += 1

        self.y += (self.current_velocity * 0.02)
