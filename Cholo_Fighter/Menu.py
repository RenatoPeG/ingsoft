import os
# import sys
import pygame
from pygame.locals import *

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


def text_render(text, font, size):
    # font_btn = pygame.font.SysFont('dolphins', 35)
    font_btn = pygame.font.Font(os.path.join('recursos', font), size)
    text_surf = font_btn.render(text, True, white)
    text_rect = text_surf.get_rect()

    return text_surf, text_rect


def load_song(name):
    fullname = os.path.join('recursos')
    fullname = os.path.join(fullname, name)
    try:
        pygame.mixer.music.load(fullname)
    except pygame.error as message:
        print('Cannot load audio file:', fullname)
        raise SystemExit(message)


def load_image(name, colorkey=None):
    fullname = os.path.join('recursos')
    fullname = os.path.join(fullname, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def music_onoff():
    if pygame.mixer.music.get_busy():
        print(pygame.mixer.music.get_busy())
        pygame.mixer.music.pause()
        pygame.mixer.music.get_pos()
    else:
        print(pygame.mixer.music.get_busy())
        pygame.mixer.music.unpause()


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
            self.button('Jugar', 150, 45, 250, 50, black, bright_green, 35, self.game_selection)
            self.button('Musica', 800, 45, 250, 50, black, bright_orange, 35, music_onoff)
            self.button('Salir', 150, 115, 250, 50, black, bright_red, 35, self.game_quit)

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

            self.button('Regresar', 30, 30, 150, 30, black, bright_orange, 20, self.game_menu)
            text_surf, text_rect = text_render("Seleccion de Personajes", 'dolphins.ttf', 70)
            text_rect.center = (self.width / 2, 100)
            self.display.blit(text_surf, text_rect)

            pygame.display.update()
            self.clock.tick(20)

    def button(self, text, x, y, width, height, in_color, ac_color, size, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.display, ac_color, (x, y, width, height))
            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(self.display, in_color, (x, y, width, height))

        text_surf, text_rect = text_render(text, 'dolphins.ttf', size)
        text_rect.center = ((x + (width / 2)), (y + (height / 2)))
        self.display.blit(text_surf, text_rect)

    @staticmethod
    def game_quit():
        pygame.quit()
        quit()


if __name__ == '__main__':
    MainWindow = Main()
    MainWindow.game_menu()
