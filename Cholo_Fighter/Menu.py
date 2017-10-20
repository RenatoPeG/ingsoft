import os
# import sys
import pygame
from pygame.locals import *
from Fisicas import *
from TextMgmt import *
from Music import *
from Imagen import *

pygame.init()

display_width = 1200
display_height = 700

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
bright_orange = (255, 100, 10)
blue_bkg = (5, 116, 218)


class Main:
    def __init__(self, width=display_width, height=display_height):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Cholo Fighter')
        self.display.fill(white)
        load_song('quiero_amanecer.mp3')
        pygame.mixer.music.play(-1, 0.0)

    def game_menu(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # fondo
            pygame.draw.rect(self.display, black, (20, 20, 1160, 660))
            # pygame.draw.rect(self.display, blue_bkg, (30, 185, 1140, 485))

            # muestra la imagen
            logo_surf, logo_rect = load_image('logo.png')
            y = display_height * 0.65
            logo_rect.center = (display_width / 2, y)
            self.display.blit(logo_surf, logo_rect)

            # botones
            button = Button('Jugar', 150, 45, 250, 50, black, bright_green, 35, self.game_selection)
            button.draw_button(self.display)
            button = Button('Musica', 800, 45, 250, 50, black, bright_orange, 35, music_onoff)
            button.draw_button(self.display)
            button = Button('Salir', 150, 115, 250, 50, black, bright_red, 35, self.game_quit)
            button.draw_button(self.display)
            button = Button('Opciones', 800, 115, 250, 50, black, bright_orange, 35, self.game_options)
            button.draw_button(self.display)

            # tasa de refresco
            pygame.display.update()
            self.clock.tick(20)

    def game_selection(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.draw.rect(self.display, black, (20, 20, 1160, 660))

            juego = MainGame()

            button = Button('Regresar', 30, 30, 150, 30, black, bright_orange, 20, self.game_menu)
            button.draw_button(self.display)
            button = Button('Jugar', 30, 400, 150, 50, black, bright_green, 35, juego.game_menu)
            button.draw_button(self.display)
            text_surf, text_rect = text_render("Seleccion de Personajes", 'dolphins.ttf', 70)
            text_rect.center = (self.width / 2, 100)
            self.display.blit(text_surf, text_rect)

            pygame.display.update()
            self.clock.tick(20)

    def game_options(self):
         while True:
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit()
                     quit()

             pygame.draw.rect(self.display, black, (20, 20, 1160, 660))

             button = Button('Regresar', 30, 30, 150, 30, black, bright_orange, 20, self.game_menu)
             button.draw_button(self.display)
             text_surf, text_rect = text_render("Opciones", 'dolphins.ttf', 70)
             text_rect.center = (self.width / 2, 100)
             self.display.blit(text_surf, text_rect)

             pygame.display.update()
             self.clock.tick(20)

    @staticmethod
    def game_quit():
        pygame.quit()
        quit()


if __name__ == '__main__':
    MainWindow = Main()
    MainWindow.game_menu()
