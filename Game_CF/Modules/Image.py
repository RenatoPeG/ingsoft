import os
import pygame

# colorkey=None en parametros


def load_image(name):
    file_path = os.path.join('Resources')
    file_path = os.path.join(file_path, name)

    try:
        image = pygame.image.load(file_path)
        image = image.convert()
        return image, image.get_rect()
    except pygame.error as message:
        print('Cannot load image:', file_path)
        raise SystemExit(message)

    # if colorkey is not None:
    #     if colorkey is -1:
    #         colorkey = image.get_at((0, 0))
    #     image.set_colorkey(colorkey, RLEACCEL)
