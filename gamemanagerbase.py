from tkinter import Tk, Label, Canvas, Button


class GameManagerBase:
    def __init__(self, width: int, height: int, color: str):
        self.window = Tk()
        self.window.title("Car Game - Python GUI Project")

        self.label = Label(self.window, text="", font=('consolas', 20))
        self.label.pack()

        self.canvas = Canvas(self.window, bg=color, height=height, width=width)
        self.canvas.pack()

        self.window.update()

        self.is_main_menu = True
        self.is_game_over = False

    def main_loop(self):
        self.init_events()

        self.__next_turn()

        self.window.mainloop()

    def init_events(self):
        pass

    def __next_turn(self):
        self.update()
        self.draw()

        if self.is_main_menu is True:
            self.display_main_menu_screen()

        elif self.is_game_over is True:
            self.display_game_over_screen()
        else:
            self.lazy_call_next_turn(16)  # Gameplay

    def update(self):
        pass

    def draw(self):
        self.canvas.delete('all')

    def lazy_call_next_turn(self, miliseconds: int):
        self.window.after(miliseconds, self.__next_turn)

    def display_main_menu_screen(self):
        self.is_main_menu = False  # TODO

        self.__next_turn()

    def display_game_over_screen(self):
        self.canvas.delete('all')

    def back_to_main_menu(self):
        self.is_main_menu = True
        self.is_game_over = False

        self._restart_gameplay()

    def restart(self):
        self.is_main_menu = False
        self.is_game_over = False

        self._restart_gameplay()

    def _restart_gameplay(self):
        self.__next_turn()
