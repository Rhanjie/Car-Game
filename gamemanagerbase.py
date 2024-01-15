from tkinter import Tk, Label, Canvas, Button, Listbox, EXTENDED, ACTIVE


class GameManagerBase:
    def __init__(self, width: int, height: int, color: str):
        self.window = Tk()
        self.window.title("Car Game - Python GUI Project")

        self.canvas = Canvas(self.window, bg=color, height=height, width=width)
        self.canvas.pack()

        self.label = Label(self.canvas, text="", font=('consolas', 20))

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
        self.canvas.delete('all')

        x = self.canvas.winfo_width() / 2
        y = self.canvas.winfo_height() / 2

        difficulty = Listbox(self.window)
        difficulty.insert(0, 'Easy (200km/h)')
        difficulty.insert(1, 'Medium (300km/h)')
        difficulty.insert(2, 'Hard (400km/h)')
        difficulty.insert(3, 'Hardcore (500km/h)')
        difficulty.selection_set(1)
        self.canvas.create_window(x, y + 60, window=difficulty)

        self.canvas.create_text(x, y - 150, font=('consolas', 40), text="Car Game", fill="white")
        self.canvas.create_text(x, y - 100, font=('consolas', 30), text="Python GUI Project", fill="white")

        button_restart = Button(self.window, text="START", relief='flat',
                                command=lambda: self.restart(self.get_velocity_from_difficulty(difficulty)))
        self.canvas.create_window(x, y - 50, window=button_restart)

        button_back = Button(self.window, text="QUIT", command=self.quit, relief='flat')
        self.canvas.create_window(x, y + 170, window=button_back)

    def display_game_over_screen(self):
        self.canvas.delete('all')

    def restart(self, max_velocity: [float, None]):
        self.is_main_menu = False
        self.is_game_over = False

        self._restart_gameplay(max_velocity)

    def back_to_main_menu(self):
        self.is_main_menu = True
        self.is_game_over = False

        self._restart_gameplay(None)

    def quit(self):
        self.window.destroy()

    def _restart_gameplay(self, max_velocity: [float, None]):
        self.__next_turn()

    @staticmethod
    def get_velocity_from_difficulty(listbox: Listbox) -> float:
        return 200 + 100 * listbox.curselection()[0]
