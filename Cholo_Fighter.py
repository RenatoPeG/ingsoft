import Cholo_Fighter.Menu

class Game():
	instance = None

	@classmethod
    def getInstance(cls):
        if cls.instance == None:
            cls.instance = Game()
        return cls.instance

    def __init__(self):
        pass

    def startGame(self):
    	menu = Menu()

    	# First window to load
    	menu.gameMenu()


if __name__ == '__main__':
	choloFighter = Game.getInstance()
	choloFighter.startGame()