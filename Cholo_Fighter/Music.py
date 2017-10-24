import os
import pygame


def loadSong(name):
    fullname = os.path.join('recursos')
    fullname = os.path.join(fullname, name)

    try:
        pygame.mixer.music.load(fullname)
    except pygame.error as message:
        print('Cannot load audio file:', fullname)
        raise SystemExit(message)

def playSong(fileName):
    filePath = 'Recursos'

    pass

def musicOnnoff():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        pygame.mixer.music.get_pos()
    else:
        pygame.mixer.music.play()
