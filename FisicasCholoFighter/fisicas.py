#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class Personaje(Sprite):
	def __init__(self):
		self.image = personaje = pygame.image.load("Imagenes/parado.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(50, 51)
		self.muerto = 0
	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_SPACE]:
			self.image = personaje = pygame.image.load("Imagenes/atacando.png").convert_alpha()
		elif ataque.rect.x > 860:
			self.image = personaje = pygame.image.load("Imagenes/parado.png").convert_alpha()

		if teclas[K_a]:
			self.image = personaje = pygame.image.load("Imagenes/puñete.png").convert_alpha()
		elif teclas[K_s]:
			self.image = personaje = pygame.image.load("Imagenes/patada.png").convert_alpha()
		elif ataque.rect.x > 860:
			self.image = personaje = pygame.image.load("Imagenes/parado.png").convert_alpha()

		if teclas[K_s]:
			self.image = personaje = pygame.image.load("Imagenes/patada.png").convert_alpha()		

		if teclas[K_LEFT]:
			self.image = personaje = pygame.image.load("Imagenes/izquierda.png").convert_alpha()
			if self.rect.x > 0:
				self.rect.x -= 2
		elif teclas[K_RIGHT]:
			self.image = personaje = pygame.image.load("Imagenes/derecha.png").convert_alpha()
			if self.rect.x < 1000:
				self.rect.x += 2

		if teclas[K_UP]:
			self.image = personaje = pygame.image.load("Imagenes/arriba.png").convert_alpha()
			if self.rect.y > 0:
				self.rect.y -= 2
		elif teclas[K_DOWN]:
			if self.rect.y < 480:
				self.image = personaje = pygame.image.load("Imagenes/abajo.png").convert_alpha()
				self.rect.y += 2

class Ataque(Sprite):
	def __init__(self):
		self.image = ataque = pygame.image.load("Imagenes/ataque.gif").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(1000, 1500)
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.rect.x > 1400:
			if teclas[K_SPACE]:
				self.rect.x = (personaje.rect.x + 60)
				self.rect.y = (personaje.rect.y + 14)
		if self.rect.x < 1700:
			self.rect.x += 2

if __name__ == '__main__':
	# Variables.
	salir = False

	# Establezco la pantalla.
	screen = pygame.display.set_mode((1200,600))

	# Establezco el título.
	pygame.display.set_caption("Entregable 1")

	# Creo dos objetos surface.
	fondo = pygame.image.load("Imagenes/AMOR.jpg").convert()

	# Objetos
	temporizador = pygame.time.Clock()
	personaje = Personaje()
	ataque = Ataque()

	# Movimiento del personaje.
	while not salir:
		personaje.update()
		ataque.update()

		# actualizacion grafica
		screen.blit(fondo, (0, 0))
		screen.blit(personaje.image, personaje.rect)
		screen.blit(ataque.image, ataque.rect)

		pygame.display.flip()

		# gestion de eventos
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				salir = True
