import pygame
import os


def text_render(text, font_param, size):
    # font_btn = font.SysFont('dolphins', 35)
    font_btn = pygame.font.Font(os.path.join('recursos', font_param), size)
    text_surf = font_btn.render(text, True, pygame.Color('white'))
    text_rect = text_surf.get_rect()

    return text_surf, text_rect

def label_render(text, font_param, size, x, y, align):
    # font_btn = font.SysFont('dolphins', 35)
    font_btn = pygame.font.Font(os.path.join('recursos', font_param), size)
    text_surf = font_btn.render(text, True, pygame.Color('white'))

    if align == 'topleft':
    	text_rect = text_surf.get_rect(topleft=(x, y))
    elif align == 'topright':
    	text_rect = text_surf.get_rect(topright=(x, y))
    else:
    	text_rect = text_surf.get_rect()
    
    return text_surf, text_rect