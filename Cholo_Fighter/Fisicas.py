import pygame
import os
from pygame.locals import *
from pygame.sprite import Sprite
from Boton import *


black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
bright_orange = (255, 100, 10)
blue_bkg = (5, 116, 218)

pygame.init()

display_width = 1200
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cholo Fighter')
display.fill(white)


def text_render(text, font, size):
    font_btn = pygame.font.SysFont('Rosewood Std', 35)
    # font_btn = pygame.font.Font(os.path.join('recursos', font), size)
    text_surf = font_btn.render(text, True, white)
    text_rect = text_surf.get_rect()

    return text_surf, text_rect


class Personaje(Sprite):
    def __init__(self):
        self.image = personaje = pygame.image.load("Imagenes/peluchin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(50, 51)
        self.muerto = 0

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]:
            self.image = personaje = pygame.image.load("Imagenes/atacando.png").convert_alpha()
        elif ataque.rect.x > 860:
            self.image = personaje = pygame.image.load("Imagenes/peluchin.png").convert_alpha()

        if teclas[K_a]:
            self.image = personaje = pygame.image.load("Imagenes/puñete.png").convert_alpha()
        elif teclas[K_s]:
            self.image = personaje = pygame.image.load("Imagenes/patada.png").convert_alpha()
        elif ataque.rect.x > 860:
            self.image = personaje = pygame.image.load("Imagenes/peluchin.png").convert_alpha()

        if teclas[K_s]:
            self.image = personaje = pygame.image.load("Imagenes/patada.png").convert_alpha()

        if teclas[K_LEFT]:
            self.image = personaje = pygame.image.load("Imagenes/izquierda.png").convert_alpha()
            if self.rect.x > 0:
                self.rect.x -= 2
        elif teclas[K_RIGHT]:
            self.image = personaje = pygame.image.load("Imagenes/derecha.png").convert_alpha()
            if self.rect.x < 1000:
                self.rect.x += 2

        if teclas[K_UP]:
            self.image = personaje = pygame.image.load("Imagenes/arriba.png").convert_alpha()
            if self.rect.y > 0:
                self.rect.y -= 2
        elif teclas[K_DOWN]:
            if self.rect.y < 480:
                self.image = personaje = pygame.image.load("Imagenes/abajo.png").convert_alpha()
                self.rect.y += 2


class Ataque(Sprite):
    def __init__(self):
        self.image = ataque = pygame.image.load("Imagenes/ataque.gif").convert_alpha()
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
fondo = pygame.image.load("Imagenes/AMOR.jpg").convert()


class MainGame:
    def __init__(self, width=display_width, height=display_height):
        pygame.init()
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()

    def game_menu(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            personaje.update()
            ataque.update()

            display.blit(fondo, (0, 0))
            display.blit(personaje.image, personaje.rect)
            display.blit(ataque.image, ataque.rect)

            # botones
            # button('Salir', 1010, 25, 125, 50, black, bright_red, 35, self.game_quit)
            button = Button('Salir', 1010, 25, 125, 50, black, bright_red, 35, self.game_quit)
            button.draw_button(display)

            # tasa de refresco
            pygame.display.update()
            self.clock.tick()

    @staticmethod
    def game_quit():
        pygame.quit()
        quit()


if __name__ == '__main__':
    MainWindow = MainGame()
    MainWindow.game_menu()