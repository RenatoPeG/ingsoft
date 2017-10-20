from pygame import *
import os


def text_render(text, font_param, size):
    # font_btn = pygame.font.SysFont('dolphins', 35)
    font_btn = font.Font(os.path.join('recursos', font_param), size)
    text_surf = font_btn.render(text, True, Color('white'))
    text_rect = text_surf.get_rect()

    return text_surf, text_rect
