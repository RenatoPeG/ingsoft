# import os
# import sys
# import pygame
# from pygame.locals import *
#
# from Game_CF.Modules.Button import *
# from Game_CF.Modules.Colors import *
# from Game_CF.Modules import Text
import ctypes
from Game_CF.Modules.ConexionDB import *
from Game_CF.Modules.Physics import *
from Game_CF.Modules.Image import *
from Game_CF.Modules.Options import *
from Game_CF.Modules.Music import *

pygame.init()


class Menu:
    def __init__(self):
        ctypes.windll.user32.SetProcessDPIAware()
        # true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
        # pygame.display.set_mode(true_res, FULLSCREEN)
        self.default_display_width = 1200
        self.default_display_height = 700

        display_info = pygame.display.Info()
        self.monitor_screen_width = display_info.current_w
        self.monitor_sreen_height = display_info.current_h

        self.current_display_width = self.default_display_width
        self.current_display_height = self.default_display_height

        self.display = pygame.display.set_mode((self.current_display_width, self.current_display_height))
        self.clock = pygame.time.Clock()
        self.display.fill(white)

        Music.load_song('quiero_amanecer.mp3')
        Music.set_volume(Option.volume)
        # pygame.mixer.music.play(-1, 0.0)

        pygame.display.set_caption('Cholo Fighter')

    def game_menu(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # fondo
            self.display.fill(white)
            pygame.draw.rect(self.display, black,
                             (20, 20, self.current_display_width - 40, self.current_display_height - 40))

            # muestra la imagen
            logo_surf, logo_rect = load_image('logo.png')
            y = self.current_display_height * 0.65
            logo_rect.center = (self.current_display_width / 2, y)
            self.display.blit(logo_surf, logo_rect)

            # botones
            font_btn_size = int(self.current_display_width * 0.029167)
            button = Button('Jugar', self.current_display_width * 0.333 - 250, self.current_display_height * 0.143 - 50,
                            250, 50, black, bright_green, font_btn_size, self.game_selection)
            button.draw_button(self.display)
            button = Button('Musica', self.current_display_width * 0.666, self.current_display_height * 0.143 - 50, 250,
                            50, black, bright_orange, font_btn_size, Music.music_onoff)
            button.draw_button(self.display)
            button = Button('Salir', self.current_display_width * 0.333 - 250, self.current_display_height * 0.243 - 50,
                            250, 50, black, bright_red, font_btn_size, self.game_quit)
            button.draw_button(self.display)
            button = Button('Opciones', self.current_display_width * 0.666, self.current_display_height * 0.243 - 50,
                            250, 50, black, bright_orange, font_btn_size, self.game_options)
            button.draw_button(self.display)

            # tasa de refresco
            pygame.display.update()
            self.clock.tick(20)

    def game_selection(self):
        conn = create_connection()
        with conn:
            personajes = select_personajes(conn)

        juego = MainGame(self.display)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.display.fill(white)
            pygame.draw.rect(self.display, black,
                             (20, 20, self.current_display_width - 40, self.current_display_height - 40))

            for i in range(0, personajes.__len__()):
                x_n = (self.current_display_width - 30 * 2) / personajes.__len__()
                xpos = 30 + i * x_n
                button = Button(personajes[i].nombre, xpos, 300, x_n, 50, black, bright_red, 27, None)
                button.draw_button(self.display)

            button = Button('Regresar', 30, 30, 150, 30, black, bright_orange, 20, self.game_menu)
            button.draw_button(self.display)
            button = Button('Jugar', (self.current_display_width - 150) / 2, 500, 150, 50, black, bright_green, 35,
                            juego.game)
            button.draw_button(self.display)

            text_surf, text_rect = text_render('Seleccion de Personajes', 'dolphins.ttf', 70)
            text_rect.center = (self.current_display_width / 2, 100)
            self.display.blit(text_surf, text_rect)

            pygame.display.update()
            self.clock.tick(20)

    def game_options(self):
        # current_display_width = width
        while True:
            # Analize events
            mousebuttonup_triggered = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    mousebuttonup_triggered = True

            # Draw background
            self.display.fill(white)
            pygame.draw.rect(self.display, black,
                             (20, 20, self.current_display_width - 40, self.current_display_height - 40))

            # Draw menu content
            button_back = Button('Regresar', 30, 30, 150, 30, black, bright_orange, 20, self.game_menu)
            button_back.draw_button(self.display)

            button_defaults = Button('Reestablecer', self.current_display_width - 180, 30, 150, 30, black,
                                     bright_orange, 20, None)
            button_defaults.draw_button(self.display)

            Text.render_label('Opciones', 'white', 'dolphins.ttf', 70, self.current_display_width / 2, 100, '',
                              self.display)

            Text.render_label('Pantalla completa', 'white', 'dolphins.ttf', 36, 50, 200, 'topleft', self.display)
            toggler_fullscreen = Option.Toggler('Sí', 'No', 'white', 'dolphins.ttf', 36, black, bright_orange,
                                                self.current_display_width - 200, 200, 150, 50, Option.fullscreen,
                                                self.display)

            Text.render_label('Volumen', 'white', 'dolphins.ttf', 36, 50, 275, 'topleft', self.display)
            numeric_up_down_volume = Option.NumericUpDown(str(int(Option.volume * 100)) + '%', 'white', 'dolphins.ttf',
                                                          36, bright_red, red, self.current_display_width - 205, 275,
                                                          30, self.display)

            Text.render_label('Tiempo límite', 'white', 'dolphins.ttf', 36, 50, 350, 'topleft', self.display)
            numeric_up_down_time_limit = Option.NumericUpDown(str(Option.timeLimit), 'white', 'dolphins.ttf', 36,
                                                              bright_red, red, self.current_display_width - 205,
                                                              350, 30, self.display)

            Text.render_label('Número de rounds', 'white', 'dolphins.ttf', 36, 50, 425, 'topleft', self.display)
            numeric_up_down_rounds = Option.NumericUpDown(str(Option.rounds), 'white', 'dolphins.ttf', 36, bright_red,
                                                          red, self.current_display_width - 205, 425, 30, self.display)

            Text.render_label('Controles Jugador 1', 'white', 'dolphins.ttf', 36, 50, 500, 'topleft', self.display)
            button_configure_player1 = Button('Configurar', self.current_display_width - 245, 500, 200, 50, black, blue,
                                              36, self.display)

            Text.render_label('Controles Jugador 2', 'white', 'dolphins.ttf', 36, 50, 575, 'topleft', self.display)
            button_configure_player2 = Button('Configurar', self.current_display_width - 245, 575, 200, 50, black, blue,
                                              36, self.display)

            # Listen for button clicked
            if mousebuttonup_triggered:
                if button_defaults.mouse_in_boundaries():
                    # Fullscreen
                    Option.fullscreen = False
                    self.current_display_width = self.default_display_width
                    self.current_display_height = self.default_display_height
                    pygame.display.set_mode((self.current_display_width, self.current_display_height))
                    # Volume
                    Option.volume = 0.50
                    Music.set_volume(Option.volume)
                    # Time limit
                    Option.timeLimit = 180
                    # Rounds
                    Option.rounds = 3
                elif toggler_fullscreen.mouse_in_boundaries():
                    Option.fullscreen = not Option.fullscreen
                    if Option.fullscreen:
                        self.current_display_width = self.monitor_screen_width
                        self.current_display_height = self.monitor_sreen_height
                        pygame.display.set_mode((self.current_display_width, self.current_display_height), FULLSCREEN)
                    else:
                        self.current_display_width = self.default_display_width
                        self.current_display_height = self.default_display_height
                        pygame.display.set_mode((self.current_display_width, self.current_display_height))
                elif numeric_up_down_volume.mouse_above_left_arrow():
                    if round(Option.volume, 2) >= 0.05:
                        Option.volume -= 0.05
                        Music.set_volume(Option.volume)
                elif numeric_up_down_volume.mouse_above_right_arrow():
                    if round(Option.volume, 2) <= 0.95:
                        Option.volume += 0.05
                        Music.set_volume(Option.volume)
                elif numeric_up_down_time_limit.mouse_above_left_arrow():
                    if int(Option.timeLimit) >= 45:
                        Option.timeLimit = str(int(Option.timeLimit) - 15)
                elif numeric_up_down_time_limit.mouse_above_right_arrow():
                    if int(Option.timeLimit) <= 165:
                        Option.timeLimit = str(int(Option.timeLimit) + 15)
                elif numeric_up_down_rounds.mouse_above_left_arrow():
                    if int(Option.rounds) >= 2:
                        Option.rounds = str(int(Option.rounds) - 1)
                elif numeric_up_down_rounds.mouse_above_right_arrow():
                    if int(Option.rounds) <= 4:
                        Option.rounds = str(int(Option.rounds) + 1)
                elif button_configure_player1.mouse_in_boundaries():
                    self.configuredPlayer = 1
                    self.gameConfigurePlayer()
                elif button_configure_player2.mouse_in_boundaries():
                    self.configuredPlayer = 2
                    self.gameConfigurePlayer()

            # Refresh
            pygame.display.update()
            self.clock.tick(20)

    @staticmethod
    def game_quit():
        pygame.quit()
        quit()
