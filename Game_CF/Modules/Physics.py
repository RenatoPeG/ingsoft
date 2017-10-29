import pygame
from Game_CF.Modules.Colors import *
from Game_CF.Modules.Text import *
from pygame.sprite import Sprite

from Game_CF.Modules.Button import *

# from Game_CF.Menu import *


pygame.init()

display1 = pygame.display.set_mode((0, 0))


class Personaje(Sprite):
    def __init__(self, nombre='', vida=100):
        self.nombre = nombre
        self.ataque = ''
        self.vida = vida
        self.image = personaje = pygame.image.load("Images/peluchin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(50, 51)
        self.muerto = 0

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]:
            self.image = personaje = pygame.image.load("Images/atacando.png").convert_alpha()
        elif ataque.rect.x > 860:
            self.image = personaje = pygame.image.load("Images/peluchin.png").convert_alpha()

        if teclas[K_a]:
            self.image = personaje = pygame.image.load("Images/puñete.png").convert_alpha()
        elif teclas[K_s]:
            self.image = personaje = pygame.image.load("Images/patada.png").convert_alpha()
        elif ataque.rect.x > 860:
            self.image = personaje = pygame.image.load("Images/peluchin.png").convert_alpha()

        # if teclas[K_s]:
        #     self.image = personaje = pygame.image.load("Images/patada.png").convert_alpha()

        if teclas[K_LEFT]:
            self.image = personaje = pygame.image.load("Images/izquierda.png").convert_alpha()
            if self.rect.x > 0:
                self.rect.x -= 2
        elif teclas[K_RIGHT]:
            self.image = personaje = pygame.image.load("Images/derecha.png").convert_alpha()
            if self.rect.x < 1000:
                self.rect.x += 2

        if teclas[K_UP]:
            self.image = personaje = pygame.image.load("Images/arriba.png").convert_alpha()
            if self.rect.y > 0:
                self.rect.y -= 2
        elif teclas[K_DOWN]:
            if self.rect.y < 480:
                self.image = personaje = pygame.image.load("Images/abajo.png").convert_alpha()
                self.rect.y += 2

    def health_bar(self, display):
        pos = (20, 25, 400, 40)
        bar_width = self.vida * 4
        bar = (20, 25, bar_width, 40)

        pygame.draw.rect(display1, pygame.Color('white'), pos, 0)
        pygame.draw.rect(display1, pygame.Color('green'), bar, 0)
        pygame.draw.rect(display1, pygame.Color('black'), pos, 5)


class Ataque(Sprite):
    def __init__(self):
        self.image = ataque = pygame.image.load("Images/ataque.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(1000, 1500)

    def update(self):
        teclas = pygame.key.get_pressed()
        if self.rect.x > 1400:
            if teclas[K_SPACE]:
                self.rect.x = (personaje.rect.x + 60)
                self.rect.y = (personaje.rect.y + 14)
        if self.rect.x < 1700:
            self.rect.x += 2


personaje = Personaje()
ataque = Ataque()
fondo = pygame.image.load("Images/AMOR.jpg").convert()


class MainGame:
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


if __name__ == '__main__':
    MainWindow = MainGame()
    MainWindow.game()
