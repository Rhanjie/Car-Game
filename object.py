from abc import ABC, abstractmethod
from tkinter import Canvas


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

    def check_collision(self, other: "Object"):
        collision_x = self.x + self.width >= other.x and other.x + other.width >= self.x
        collision_y = self.y + self.height >= other.y and other.y + other.height >= self.y

        return collision_x and collision_y
