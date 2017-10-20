import os
import pygame


def load_song(name):
    fullname = os.path.join('recursos')
    fullname = os.path.join(fullname, name)
    try:
        pygame.mixer.music.load(fullname)
    except pygame.error as message:
        print('Cannot load audio file:', fullname)
        raise SystemExit(message)


def music_onoff():
    if pygame.mixer.music.get_busy():
        print(pygame.mixer.music.get_busy())
        pygame.mixer.music.stop()
        pygame.mixer.music.get_pos()
    else:
        print(pygame.mixer.music.get_busy())
        pygame.mixer.music.play()
