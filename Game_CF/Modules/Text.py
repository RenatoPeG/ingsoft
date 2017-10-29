import pygame
import os


def text_render(text, font_param, size):
    pygame.font.init()
    # font_btn = font.SysFont('dolphins', 35)
    font_btn = pygame.font.Font(os.path.join('Resources', font_param), size)
    text_surf = font_btn.render(text, True, pygame.Color('white'))
    text_rect = text_surf.get_rect()

    return text_surf, text_rect


def render_label(text, color, font_family, font_size, x, y, align, display):
    font = pygame.font.Font('Resources/%s' % font_family, font_size)
    label = font.render(text, True, pygame.Color(color))

    if align == 'topleft':
        label_rect = label.get_rect(topleft=(x, y))
    elif align == 'topright':
        label_rect = label.get_rect(topright=(x, y))
    else:
        label_rect = label.get_rect()
        label_rect.center = (x, y)

    display.blit(label, label_rect)
