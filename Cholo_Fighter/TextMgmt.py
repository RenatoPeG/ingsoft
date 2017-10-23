import pygame
import os


def text_render(text, font_param, size):
    # font_btn = font.SysFont('dolphins', 35)
    font_btn = pygame.font.Font(os.path.join('recursos', font_param), size)
    text_surf = font_btn.render(text, True, pygame.Color('white'))
    text_rect = text_surf.get_rect()

    return text_surf, text_rect
