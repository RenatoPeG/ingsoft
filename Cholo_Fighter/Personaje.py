from pygame import *


class Personaje1:
    def __init__(self, nombre='', ataques='', vida=100, caracter_img=''):
        self.nombre = nombre
        self.ataques = ataques
        self.vida = vida
        self.caracter_img = caracter_img

    def health_bar(self, display):
        pos = (20, 25, 400, 40)
        bar_width = self.vida * 3
        bar = (20, 25, bar_width, 40)

        draw.rect(display, Color('white'), pos, 0)
        draw.rect(display, Color('green'), bar, 0)
        draw.rect(display, Color('black'), pos, 5)

