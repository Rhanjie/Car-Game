from tkinter import LEFT, RIGHT, Button

from gamemanagerbase import GameManagerBase
from terrain import Terrain
from player import Player


class GameManager(GameManagerBase):
    def __init__(self, width: int, height: int, color: str):
        GameManagerBase.__init__(self, width, height, color)

        self.player = Player(int(width / 2), 500, "#00FF00", 300)
        self.terrain = Terrain("#ffffff", 300, width, height)

        self.current_distance = self.player.y

    def init_events(self):
        self.window.bind('<Left>', lambda event: self.player.change_direction(LEFT))
        self.window.bind('<Right>', lambda event: self.player.change_direction(RIGHT))

    def update(self):
        GameManagerBase.update(self)

        self.current_distance = self.player.vertical_distance
        self.terrain.update(self.current_distance)
        self.player.update(self.current_distance)

        if self.terrain.check_collisions(self.player):
            self.is_game_over = True

    def draw(self):
        GameManagerBase.draw(self)

        self.draw_ui()

        self.terrain.draw(self.canvas, self.player.vertical_distance)
        self.player.draw(self.canvas, 0)

    def draw_ui(self):
        current_distance = self.player.vertical_distance

        self.canvas.create_text(680, 200, font=('consolas', 20), text="Distance\n{}m".format(int(current_distance)), fill="white")
        self.canvas.create_text(680, 300, font=('consolas', 20), text="{} km/h".format(self.player.current_velocity), fill="white")

    def _restart_gameplay(self, max_velocity: [float, None]):
        self.terrain.start()
        self.player.start(max_velocity)

        GameManagerBase._restart_gameplay(self, max_velocity)

    def display_game_over_screen(self):
        GameManagerBase.display_game_over_screen(self)

        x = self.canvas.winfo_width() / 2
        y = self.canvas.winfo_height() / 2
        distance = self.player.vertical_distance

        self.canvas.create_text(x, y - 10, font=('consolas', 70), text="GAME OVER", fill="red")
        self.canvas.create_text(x, y + 60, font=('consolas', 30), text="Distance: {}m".format(distance), fill="green")

        self.canvas.create_line(x - 300, y + 100, x + 300, y + 100, fill="white")

        button_restart = Button(self.window, text="RESTART", command=lambda: self.restart(None), relief='flat')
        self.canvas.create_window(x - 100, y + 140, window=button_restart)

        button_back = Button(self.window, text="BACK TO MAIN MENU", command=self.back_to_main_menu, relief='flat')
        self.canvas.create_window(x + 100, y + 140, window=button_back)
