from tkinter import LEFT, RIGHT

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

        current_distance = self.player.vertical_distance

        self.label.config(text="Points:{} - {} km/h".format(int(current_distance), self.player.current_velocity))

        self.terrain.draw(self.canvas, current_distance)
        self.player.draw(self.canvas, 0)
