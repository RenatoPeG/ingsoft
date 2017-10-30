#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

#/////////////////////////////////////////////--- PERSONAJE 1 ---///////////////////////////////////////
class Personaje1(Sprite):
	def __init__(self):
		self.image = personaje1 = pygame.image.load("Melcocha/melcochita1.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(50, 240)
		self.muerto = 0
	def update(self):
		teclas = pygame.key.get_pressed()
		#//////////////////// BOTON PARA ATQUE ESPECIAL PJ1 ////////////////////////
		if teclas[K_SPACE]:
			self.image = personaje1 = pygame.image.load("Melcocha/melcochita7.png").convert_alpha()
		elif ataque.rect.x > 860:
			self.image = personaje1 = pygame.image.load("Melcocha/melcochita1.png").convert_alpha()
		#//////////////////// BOTONES PARA GOLPES BÁSICOS PJ1 //////////////////////
		if teclas[K_r]:
			self.image = personaje1 = pygame.image.load("Melcocha/melcochita2.png").convert_alpha()
		elif teclas[K_t]:
			self.image = personaje1 = pygame.image.load("Melcocha/melcochita3.png").convert_alpha()
		elif ataque.rect.x > 860:
			self.image = personaje1 = pygame.image.load("Melcocha/melcochita1.png").convert_alpha()
		#//////////////////// BOTONES PARA MOVERSE PJ1 /////////////////////////////
		if teclas[K_a]:
			self.image = personaje1 = pygame.image.load("Melcocha/melcochita1inv.png").convert_alpha()
			if self.rect.x > 0:
				self.rect.x -= 2
		elif teclas[K_d]:
			self.image = personaje1 = pygame.image.load("Melcocha/melcochita1.png").convert_alpha()
			if self.rect.x < 1140:
				self.rect.x += 2
		if teclas[K_w]:
			self.image = personaje1 = pygame.image.load("Melcocha/melcochita5.png").convert_alpha()
			if self.rect.y > 0:
				self.rect.y -= 2
		elif teclas[K_s]:
			if self.rect.y < 240:
				self.image = personaje1 = pygame.image.load("Melcocha/melcochita6.png").convert_alpha()
				self.rect.y += 2
			
#ATAQUE PERSONAJE 1
class AtaqueP1(Sprite):
	def __init__(self):
		self.image = ataque = pygame.image.load("Melcocha/lanzamientomelcochita.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(1000, 1500)
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.rect.x > 1400:
			if teclas[K_SPACE]:
				self.rect.x = (personaje1.rect.x + 60)
				self.rect.y = (personaje1.rect.y + 14)
		if self.rect.x < 1700:
			self.rect.x += 2			

#VIDA PERSONAJE 1
class BarraVidaPJ1(Sprite):
	def __init__(self):
		self.image = barravidapj1 = pygame.image.load("Imagenes/barravidapj1.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(50, 20)
	def update(self):
		if barravidapj1.rect.x <= -152:
			personaje1.muerto = 1
		if disparo.rect.y >= (personaje1.rect.y - 56):
			if disparo.rect.y <= (personaje1.rect.y + 62):
				if disparo.rect.x >= personaje1.rect.x:
					if disparo.rect.x <= (personaje1.rect.x + 43):
						barravidapj1.rect.x -= 26
						disparo.rect.x = -400
		if minicell.rect.y >= (personaje1.rect.y - 56):
			if minicell.rect.y <= (personaje1.rect.y + 62):
				if minicell.rect.x >= personaje1.rect.x:
					if minicell.rect.x <= (personaje1.rect.x + 43):
						barravidapj1.rect.x -= 26
						disparo.rect.x = -400

#/////////////////////////////////////////////--- PERSONAJE 2 ---///////////////////////////////////////

class Personaje2(Sprite):
	def __init__(self):
		self.image = personaje2 = pygame.image.load("Magaly/parado_izq_magaly.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(1000, 240)
		self.muerto = 0
	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_i]:
			self.image = personaje2 = pygame.image.load("Magaly/atacando_izq_magaly.png").convert_alpha()
		elif ataque.rect.x > 860:
			self.image = personaje2 = pygame.image.load("Magaly/parado_izq_magaly.png").convert_alpha()

		if teclas[K_p]:
			self.image = personaje2 = pygame.image.load("Magaly/puñete.png").convert_alpha()
		elif teclas[K_o]:
			self.image = personaje2 = pygame.image.load("Magaly/patada.png").convert_alpha()
		elif ataque.rect.x > 860:
			self.image = personaje2 = pygame.image.load("Magaly/parado_izq_magaly.png").convert_alpha()

		if teclas[K_LEFT]:
			self.image = personaje2 = pygame.image.load("Magaly/derecha_magaly_p2.png").convert_alpha()
			if self.rect.x > 0:
				self.rect.x -= 2
		elif teclas[K_RIGHT]:
			self.image = personaje2 = pygame.image.load("Magaly/derecha_magaly_p1.png").convert_alpha()
			if self.rect.x < 1140:
				self.rect.x += 2

		if teclas[K_UP]:
			self.image = personaje2 = pygame.image.load("Magaly/magaly_arriba_izq.png").convert_alpha()
			if self.rect.y > 0:
				self.rect.y -= 2
		elif teclas[K_DOWN]:
			if self.rect.y < 240:
				self.image = personaje2 = pygame.image.load("Magaly/magaly_abajo_izq.png").convert_alpha()
				self.rect.y += 2

#ATAQUE PERSONAJE 2
class Disparo(Sprite):
	def __init__(self):
		self.image = barravidapj1 = pygame.image.load("Imagenes/disparominicell.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(-400, -400)
	def update(self):
		if self.rect.x == -400:
			if personaje2.rect.y == personaje1.rect.y:
				self.rect.x = (minicell.rect.x - 60)
				self.rect.y = (minicell.rect.y - 14)
		if self.rect.x > -400:
			self.rect.x -= 5


if __name__ == '__main__':
	# Variables.
	salir = False

	# Establezco la pantalla.
	screen = pygame.display.set_mode((1200,363))

	# Establezco el título.
	pygame.display.set_caption("Entregable 4")

	# Creo dos objetos surface.
	fondo = pygame.image.load("Imagenes/fondo1.png").convert()
	vidapj1 = pygame.image.load("Imagenes/cuadrovidapj1.png").convert_alpha()

	# Objetos
	temporizador = pygame.time.Clock()
	personaje1 = Personaje1()
	personaje2 = Personaje2()
	ataque = AtaqueP1()
	barravidapj1 = BarraVidaPJ1()

	# Movimiento del personaje.
	while not salir:
		personaje1.update()
		personaje2.update()
		ataque.update()

		# actualizacion grafica
		screen.blit(fondo, (0, 0))
		screen.blit(personaje1.image, personaje1.rect)
		screen.blit(personaje2.image, personaje2.rect)
		screen.blit(ataque.image, ataque.rect)
		screen.blit(barravidapj1.image, barravidapj1.rect)

		pygame.display.flip()

		# gestion de eventos
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				salir = True
