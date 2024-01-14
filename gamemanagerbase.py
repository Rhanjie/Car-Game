from tkinter import Tk, Label, Canvas


class GameManagerBase:
    def __init__(self, width: int, height: int, color: str):
        self.window = Tk()
        self.window.title("Car Game - Python GUI Project")

        self.label = Label(self.window, text="", font=('consolas', 20))
        self.label.pack()

        self.canvas = Canvas(self.window, bg=color, height=height, width=width)
        self.canvas.pack()

        self.window.update()

    def main_loop(self):
        self.init_events()

        self.__next_turn()

        self.window.mainloop()

    def init_events(self):
        pass

    def __next_turn(self):
        self.update()
        self.draw()

        self.lazy_call_next_turn(16)

    def update(self):
        pass

    def draw(self):
        self.canvas.delete('all')

    def lazy_call_next_turn(self, miliseconds: int):
        self.window.after(miliseconds, self.__next_turn)
