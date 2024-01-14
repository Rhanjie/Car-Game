from gamemanager import GameManager

if __name__ == '__main__':
    width = 800
    height = 600

    game_manager = GameManager(800, 600, "#000000")
    game_manager.main_loop()
