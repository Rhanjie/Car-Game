import random
from tkinter import Canvas

from line import Line
from obstacle import Obstacle


class Terrain:
    def __init__(self, lines_color: str, road_width: int, screen_width: int, screen_height: int):
        self.lines_color = lines_color
        self.background_items = []
        self.obstacles = []

        self.road_width = road_width
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.total_obstacles_spawned = 0
        self.total_centered_lines_spawned = -4

        # Draw previous lines on the start
        self.spawn_road_cropped_line(-600)
        self.spawn_road_cropped_line(-450)
        self.spawn_road_cropped_line(-300)
        self.spawn_road_cropped_line(-150)

    def update(self, current_y: int):
        self.background_items[:] = [item for item in self.background_items if not item.ready_to_delete(current_y)]
        self.obstacles[:] = [obstacle for obstacle in self.obstacles if not obstacle.ready_to_delete(current_y)]

        self.spawn_obstacle(current_y)
        self.spawn_road_cropped_line(current_y)

    def draw(self, canvas: Canvas, current_y: int):
        for item in self.background_items:
            item.draw(canvas, current_y)

        for obstacle in self.obstacles:
            obstacle.draw(canvas, current_y)

        self.draw_road_side_lines(canvas)

    def spawn_obstacle(self, current_y: int):
        should_spawn = (current_y / 200 > self.total_obstacles_spawned)
        if not should_spawn:
            return

        offset = int((self.screen_width - self.road_width) / 2)

        position_x = random.randint(offset, self.screen_width - offset)
        self.obstacles.append(Obstacle(position_x, current_y, "#FFFF00"))
        self.total_obstacles_spawned += 1

    def spawn_road_cropped_line(self, current_y: int):
        should_spawn = (current_y / 150 > self.total_centered_lines_spawned)
        if not should_spawn:
            return

        position_x = self.screen_width / 2
        self.obstacles.append(Line(position_x, current_y, self.lines_color))
        self.total_centered_lines_spawned += 1

    def draw_road_side_lines(self, canvas: Canvas):
        offset = int((self.screen_width - self.road_width) / 2) - 30
        side_line_x1 = offset
        side_line_x2 = self.screen_width - offset

        canvas.create_rectangle(
            side_line_x1, 0, side_line_x1 + 5, self.screen_height, fill=self.lines_color)

        canvas.create_rectangle(
            side_line_x2, 0, side_line_x2 + 5, self.screen_height, fill=self.lines_color)
