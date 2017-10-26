from pygame import *

from Cholo_Fighter.Modules.TextMgmt import *


class Button:
    def __init__(self, text='', x=0, y=0, width=0, height=0, in_color='', ac_color='', size=0, action=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.in_color = in_color
        self.ac_color = ac_color
        self.size = size
        self.action = action

    def draw_button(self, display):
        mouse_pos = mouse.get_pos()
        click = mouse.get_pressed()

        if self.x + self.width > mouse_pos[0] > self.x and self.y + self.height > mouse_pos[1] > self.y:
            draw.rect(display, self.ac_color, (self.x, self.y, self.width, self.height))
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            draw.rect(display, self.in_color, (self.x, self.y, self.width, self.height))

        text_surf, text_rect = text_render(self.text, 'dolphins.ttf', self.size)
        text_rect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
        display.blit(text_surf, text_rect)
