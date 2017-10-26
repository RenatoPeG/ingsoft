from Cholo_Fighter.Modules.Menu import *


class Game:
    def __init__(self):
        pass

    def start_game(self):
        menu = Menu()

        # Loading game
        menu.game_menu()


if __name__ == '__main__':
    choloFighter = Game()
    choloFighter.start_game()
