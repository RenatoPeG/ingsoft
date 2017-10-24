# import os
# import sys
# import pygame
import Music
from Imagen import *
from ConexionDB import *
from Opciones import *

pygame.init()

class Main:
    def __init__(self):
        # Default display settings
        self.defaultDisplayWidth = 1200
        self.defaultDisplayHeight = 700

        # Get monitor size info
        displayInfo = pygame.display.Info()
        self.monitorScreenWidth = displayInfo.current_w
        self.monitorScreenHeight = displayInfo.current_h

        # Set display starting configuration
        self.currentDisplayWidth = self.defaultDisplayWidth
        self.currentDisplayHeight = self.defaultDisplayHeight

        # Initialize display
        pygame.display.set_mode((self.currentDisplayWidth, self.currentDisplayHeight))
        pygame.display.set_caption('Cholo Fighter')
        pygame.display.fill(white)

        # Play music
        Music.loadSong('quiero_amanecer.mp3')
        pygame.mixer.music.play(-1, 0.0)

        self.width = width
        self.height = height
        fsInfo = pygame.display.Info()
        self.fsWidth = fsInfo.current_w
        self.fsHeight = fsInfo. current_h
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Cholo Fighter')
        self.display.fill(white)
        load_song('quiero_amanecer.mp3')
        pygame.mixer.music.play(-1, 0.0)
        ctrlJ1 = ControlesK(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_l, pygame.K_i, pygame.K_o)
        ctrlJ2 = ControlesK(pygame.K_r, pygame.K_f, pygame.K_d, pygame.K_g, pygame.K_x, pygame.K_a, pygame.K_s)
        self.opciones = Opciones(False, 0.5, 180, 3, ctrlJ1, ctrlJ2);

    def gameMenu(self):
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
        conn = create_connection()
        with conn:
            personajes = select_personajes(conn)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.draw.rect(self.display, black, (20, 20, 1160, 660))

            juego = MainGame()

            # for i in range(0, personajes.__len__()):
            #     xpos = (self.width / personajes.__len__()) / 2 + (self.width / personajes.__len__()) * i  # (x/n)(i+0.5)
            #     # nombre
            #     text_surf, text_rect = text_render(personajes[i].nombre, 'dolphins.ttf', 20)
            #     text_rect.center = (xpos, 300)
            #     self.display.blit(text_surf, text_rect)
            #     #vida
            #     text_surf, text_rect = text_render(str(personajes[i].vida), 'dolphins.ttf', 20)
            #     text_rect.center = (xpos, 350)
            #     self.display.blit(text_surf, text_rect)

            for i in range(0, personajes.__len__()):
                x_n = (self.width - 30 * 2) / personajes.__len__()
                xpos = 30 + i * x_n
                button = Button(personajes[i].nombre, xpos, 300, x_n, 50, black, bright_red, 27, None)
                button.draw_button(self.display)

            button = Button('Regresar', 30, 30, 150, 30, black, bright_orange, 20, self.game_menu)
            button.draw_button(self.display)
            button = Button('Jugar', (self.width-150)/2, 500, 150, 50, black, bright_green, 35, juego.game_menu)
            button.draw_button(self.display)

            text_surf, text_rect = text_render('Seleccion de Personajes', 'dolphins.ttf', 70)
            text_rect.center = (self.width / 2, 100)
            self.display.blit(text_surf, text_rect)

            pygame.display.update()
            self.clock.tick(20)

    def game_options(self):
        while True:
            mousebuttonupPressed = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    mousebuttonupPressed = True


            pygame.draw.rect(self.display, black, (20, 20, 1160, 660))
            button = Button('Regresar', 30, 30, 150, 30, black, bright_orange, 20, self.game_menu)
            button.draw_button(self.display)

            text_surf, text_rect = label_render('Pantalla completa', 'dolphins.ttf', 36, 50, 200, 'topleft')
            self.display.blit(text_surf, text_rect)
            fsToggler = Toggler(self.display, display_width - 200, 200, 150, 30, 36, black, bright_orange, 'Sí', 'No', self.opciones.fullscreen)
            if mousebuttonupPressed and fsToggler.mouseInBonudaries():
                self.opciones.fullscreen = not self.opciones.fullscreen
                if self.opciones.fullscreen:
                    pygame.display.set_mode((self.fsWidth, self.fsHeight), pygame.FULLSCREEN)
                else:
                    pygame.display.set_mode((self.width, self.height))

            text_surf, text_rect = label_render('Volumen', 'dolphins.ttf', 36, 50, 300, 'topleft')
            self.display.blit(text_surf, text_rect)


            text_surf, text_rect = label_render('Tiempo límite', 'dolphins.ttf', 36, 50, 400, 'topleft')
            self.display.blit(text_surf, text_rect)


            text_surf, text_rect = label_render('Número de rounds', 'dolphins.ttf', 36, 50, 500, 'topleft')
            self.display.blit(text_surf, text_rect)


            text_surf, text_rect = label_render('Controles Jugador 1', 'dolphins.ttf', 36, 50, 600, 'topleft')
            self.display.blit(text_surf, text_rect)


            text_surf, text_rect = label_render('Controles Jugador 2', 'dolphins.ttf', 36, 50, 700, 'topleft')
            self.display.blit(text_surf, text_rect)           


            
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
