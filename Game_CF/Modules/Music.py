import os
import pygame


class Music:
    @staticmethod
    def load_song(name):
        fullname = os.path.join('Resources')
        fullname = os.path.join(fullname, name)
        try:
            pygame.mixer.music.load(fullname)
        except pygame.error as message:
            print('Cannot load audio file:', fullname)
            raise SystemExit(message)

    @staticmethod
    def music_onoff():
        if pygame.mixer.music.get_busy():
            print(pygame.mixer.music.get_busy())
            pygame.mixer.music.stop()
            pygame.mixer.music.get_pos()
        else:
            print(pygame.mixer.music.get_busy())
            pygame.mixer.music.play()

    @staticmethod
    def set_volume(value):
        pygame.mixer.music.set_volume(value)
