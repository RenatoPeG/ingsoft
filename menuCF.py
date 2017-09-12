import os, sys
import pygame
from pygame.locals import *

pygame.init()

display_width = 1200
display_height = 700

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0 , 200)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
bright_orange = (255, 100, 10)
blue_bkg = (5, 116, 218)


def text_render(text, font):
    textSurface = font.render(text, True, black)
    return textSurfface, textSurfcae.get_rect()

def load_song(name):
    fullname = os.path.join('recursos')
    fullname = os.path.join(fullname, name)
    try:
        song = pygame.mixer.music.load(fullname)
    except pygame.error as message:
        print('Cannot load audio file:', fullname)
        raise SystemExit(message)

def load_image(name, colorkey=None):
    fullname = os.path.join('recursos')
    fullname = os.path.join(fullname, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print ('Cannot load image:', fullname)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Main:
    def __init__(self, width = display_width, height = display_height):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Cholo Fighter')
        self.display.fill(white)
        load_song('quiero_amanecer.mp3')
        pygame.mixer.music.play(-1, 0.0)

    def game_Menu(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            '''TEXTO EN MEDIO DE PANTALLA
            self.display.fill(white)
            font = pygame.font.Font('freesansbold.ttf', 115)
            textSurface = font.render('Cholo Fighter', True, black)
            textRect = textSurface.get_rect()
            textRect.center = ((display_width / 2), (display_height / 2))
            self.display.blit(textSurface, textRect)
            '''

            #fondo
            pygame.draw.rect(self.display, black, (20, 20, 1160, 660))
            #pygame.draw.rect(self.display, blue_bkg, (30, 185, 1140, 485))

            #muestra la imagen
            logoSurf, logoRect = load_image('logo.png')
            y = display_height * 0.7
            logoRect.center = ((display_width / 2, y))
            self.display.blit(logoSurf, logoRect)

            #botones
            self.button('Un Jugador', 150, 45, 250, 50, black, bright_green, self.game_quit)
            self.button('Musica', 800, 45, 250, 50, black, bright_orange, self.music_onoff)
            #self.button('Multijugador', 150, 70, 250, 50, black, bright_green, self.game_quit)
            #self.button('Historia', 150, 130, 250, 50, black, bright_green, self.game_quit)
            self.button('Salir', 150, 115, 250, 50, black, bright_red, self.game_quit)

            #tasa de refresco
            pygame.display.update()
            self.clock.tick(20)

    def button(self, text, x, y, width, height, inColor, acColor, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+width > mouse[0] > x and y+height > mouse[1] > y:
            pygame.draw.rect(self.display, acColor, (x, y, width, height))
            if click[0] == 1 and action is not None:
                action ()
        else:
            pygame.draw.rect(self.display, inColor, (x, y, width, height))

        #fontBtn = pygame.font.SysFont('dolphins', 35)
        fontBtn = pygame.font.Font(os.path.join('recursos', 'dolphins.ttf'), 35)
        textSurf = fontBtn.render(text, True, white)
        textRect = textSurf.get_rect()
        textRect.center = ((x + (width / 2)), (y + (height / 2)))
        self.display.blit(textSurf, textRect)

    def music_onoff(self):
        if pygame.mixer.music.get_busy():
            print(pygame.mixer.music.get_busy())
            pygame.mixer.music.stop()
            pausa = pygame.mixer.music.get_pos()
        else:
            print(pygame.mixer.music.get_busy())
            pygame.mixer.music.play(-1)

    def game_quit(self):
        pygame.quit()
        quit()


if __name__ == '__main__':
    MainWindow = Main()
    MainWindow.game_Menu()
