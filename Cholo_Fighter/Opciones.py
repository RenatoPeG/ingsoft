from pygame import *
from TextMgmt import *

def modificar_control():
    pass

class ControlesK():
    def __init__(self, mArriba, mAbajo, mIzquierda, mDerecha, saltar, gBasicoP, gBasicoS):
        self.mArriba = mArriba
        self.mAbajo = mAbajo
        self.mIzquierda = mIzquierda
        self.mDerecha = mDerecha
        self.saltar = saltar
        self.gBasicoP = gBasicoP
        self.gBasicoS = gBasicoS
        self.pBasico = [self.mArriba, self.mAbajo, self.gBasicoP]
        self.pEspec = [self.mArriba, self.mAbajo, self.gBasicoS, self.mDerecha]

class Opciones():
    def __init__(self, fullscreen, volume, tLimit, nRounds, ctrlJ1, ctrlJ2):
        self.fullscreen = fullscreen
        self.volume = volume
        self.tLimit = tLimit
        self.nRounds = nRounds
        self.ctrlJ1 = ctrlJ1
        self.ctrlJ2 = ctrlJ2

class Toggler():
    def __init__(self, display, x, y, width, height, font_size, color, focus_color, textIfTrue, textIfFalse, toggled):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        
        mouse_pos = mouse.get_pos()
        if self.x + self.width > mouse_pos[0] > self.x and self.y + self.height > mouse_pos[1] > self.y:
            draw.rect(display, focus_color, (self.x, self.y, self.width, self.height))
        else:
            draw.rect(display, color, (self.x, self.y, self.width, self.height))

        text = None
        if toggled:
            text = textIfTrue
        else:
            text = textIfFalse

        text_surf, text_rect = text_render(text, 'dolphins.ttf', font_size)
        text_rect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
        display.blit(text_surf, text_rect)

    def mouseInBonudaries(self):
        mouse_pos = mouse.get_pos()
        return (self.x + self.width > mouse_pos[0] > self.x and self.y + self.height > mouse_pos[1] > self.y)