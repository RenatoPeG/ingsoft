import pygame
import os

#MODIFICAR CONTROL

#Crear funcion que modifique control
def modificar_control():


#Atar funcion a los botones de configuracion de la pantalla




#REESTABLECER PREDETERMINADOS


#Crear diccionario de controles predeterminados
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
        self.pEspec = [self.mArriba, self.mAabajo, self.gBasicoS, self.mDerecha]


ctrlJ1 = ControlesK(K_UP, K_DOWN, K_LEFT, K_RIGHT, K_l, K_i, K_o)
ctrlJ2 = ControlesK(K_r, K_f, K_d, K_g, K_x, K_a, K_s)

#Implementar boton que aplique diccionario a botones predeterminados



#CONFIGURAR OPCIONES DE JUEGO


#Crear diccionario de opciones del juego
class Opciones():
    def __init__(self, fullscreen, volume, tLimit, nRounds, ctrlJ1, ctrlJ2):
        self.fullscreen = fullscreen
        self.volume = volume
        self.tLimit = tLimit
        self.nRounds = nRounds
        self.ctrlJ1 = ctrlJ1
        self.ctrlJ2 = ctrlJ2


gOptions = Opciones(false, 0.5, 180, 3, ctrlJ1, ctrlJ2)

#Maquetar pantalla de configuracion de opciones de juego

#Crear funcion que modifique una opciones

#Atar funcion a los botones de configuracion de la pantalla
