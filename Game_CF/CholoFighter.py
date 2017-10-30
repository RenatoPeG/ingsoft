from Game_CF.Modules.Menu import *


class Game:
    def __init__(self):
        pass

    @staticmethod
    def start_game():
        menu = Menu()

        # Loading game
        menu.game_menu()


if __name__ == '__main__':
    choloFighter = Game()
    choloFighter.start_game()
