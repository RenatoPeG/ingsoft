import pygame
from Game_CF.Modules.Menu import *


pygame.init()
display1 = pygame.display.set_mode((0, 0))


class Game:
    def __init__(self, cant_rondas=0, tiempo=0, personajes=None, display=None):
        self.cant_rondas = cant_rondas
        self.tiempo = tiempo
        self.personajes = personajes
        self.display = display

    def __init__(self, display):
        pygame.init()
        self.display = display
        self.clock = pygame.time.Clock()

    def game(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            personaje.update()
            ataque.update()
            self.display.blit(fondo, (0, 0))
            self.display.blit(personaje.image, personaje.rect)
            self.display.blit(ataque.image, ataque.rect)
            personaje.health_bar(display)

            # botones
            # button('Salir', 1010, 25, 125, 50, black, bright_red, 35, self.game_quit)
            button = Button('Salir', 1010, 25, 125, 50, black, bright_red, 35, self.game_quit)
            button.draw_button(self.display)

            # tasa de refresco
            pygame.display.update()
            self.clock.tick()

    @staticmethod
    def game_quit():
        pygame.quit()
        quit()