from tkinter import Canvas

from object import Object


class Obstacle(Object):
    def __init__(self, x: int, y: int, color: str):
        Object.__init__(self, x, y, color)

        self.display_y = self.y

    def update(self, current_y: int):
        self.display_y = current_y - self.y

    def draw(self, canvas: Canvas, current_y: int):
        canvas.create_rectangle(
            self.x, self.display_y - self.height, self.x + self.width, self.display_y, fill=self.color)
