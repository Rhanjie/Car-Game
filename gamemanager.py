from tkinter import LEFT, RIGHT

from gamemanagerbase import GameManagerBase
from terrain import Terrain
from player import Player


class GameManager(GameManagerBase):
    def __init__(self, width: int, height: int, color: str):
        GameManagerBase.__init__(self, width, height, color)

        self.player = Player(int(width / 2), 0, "#00FF00", 300, 500)
        self.terrain = Terrain("#ffffff", 300, width, height)

    def init_events(self):
        self.window.bind('<Left>', lambda event: self.player.change_direction(LEFT))
        self.window.bind('<Right>', lambda event: self.player.change_direction(RIGHT))

    def update(self):
        GameManagerBase.update(self)

        self.terrain.update(self.player.y)
        self.player.update(0)

    def draw(self):
        GameManagerBase.draw(self)

        self.label.config(text="Points:{} - {}".format(self.player.y, self.player.current_velocity))

        self.terrain.draw(self.canvas, self.player.y)
        self.player.draw(self.canvas, 0)
