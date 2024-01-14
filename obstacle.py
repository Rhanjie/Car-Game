from tkinter import Canvas

from object import Object


class Obstacle(Object):
    def __init__(self, x: int, y: int, color: str):
        Object.__init__(self, x, y, color)

    def update(self, current_y: int):
        pass

    def draw(self, canvas: Canvas, current_y: int):
        y_screen = current_y - self.y

        square = canvas.create_rectangle(
            self.x, y_screen - self.height, self.x + self.width, y_screen, fill=self.color)
