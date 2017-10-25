import pygame

class Music:
	@staticmethod
	def playSong(fileName):
		filePath = 'Resources/%s' % fileName
		try:
			pygame.mixer.music.load(filePath)
			pygame.mixer.music.play(-1, 0.0)
		except pygame.error as message:
			print('Cannot load audio file:', fileName)
			raise SystemExit(message)

	@staticmethod
	def toggleMusic():
		if pygame.mixer.music.get_busy():
			pygame.mixer.music.stop()
			pygame.mixer.music.get_pos()
		else:
			pygame.mixer.music.play()

	@staticmethod
	def setVolume(value):
		pygame.mixer.music.set_volume(value)