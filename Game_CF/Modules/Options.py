import pygame

from Game_CF.Modules import Text


class Option:
    class Control:
        def __init__(self, move_up, move_down, move_left, move_right, jump, primary_basic_attack,
                     secondary_basic_attack):
            self.moveUp = move_up
            self.moveDown = move_down
            self.moveLeft = move_left
            self.moveRight = move_right
            self.jump = jump
            self.primaryBasicAttack = primary_basic_attack
            self.secondaryBasicAttack = secondary_basic_attack
            self.basicPower = [self.moveUp, self.moveDown, self.primaryBasicAttack]
            self.specialPower = [self.moveUp, self.moveDown, self.secondaryBasicAttack, self.moveRight]

        def update_basic_special_power(self):
            self.basicPower = [self.moveUp, self.moveDown, self.primaryBasicAttack]
            self.specialPower = [self.moveUp, self.moveDown, self.secondaryBasicAttack, self.moveRight]

    class Toggler:
        def __init__(self, text_if_true, text_if_false, color, font_family, font_size, background_color,
                     background_color_hover, x, y, width, height, toggled, display):
            self.x = x
            self.y = y
            self.width = width
            self.height = height

            mouse_pos = pygame.mouse.get_pos()
            if self.x + self.width > mouse_pos[0] > self.x and self.y + self.height > mouse_pos[1] > self.y:
                pygame.draw.rect(display, background_color_hover, (self.x, self.y, self.width, self.height))
            else:
                pygame.draw.rect(display, background_color, (self.x, self.y, self.width, self.height))

            # text = None
            if toggled:
                text = text_if_true
            else:
                text = text_if_false

            Text.render_label(text, color, font_family, font_size, (self.x + (self.width / 2)),
                              (self.y + (self.height / 2)), '', display)

        def mouse_in_boundaries(self):
            mouse_pos = pygame.mouse.get_pos()
            return self.x + self.width > mouse_pos[0] > self.x and self.y + self.height > mouse_pos[1] > self.y

    class NumericUpDown:
        def __init__(self, text, color, font_family, font_size, background_color, background_color_hover, x, y, height,
                     display):
            self.x = x
            self.y = y
            self.height = height

            mouse_pos = pygame.mouse.get_pos()
            # Above left arrow
            if self.x + 25 > mouse_pos[0] > self.x and self.y + self.height > mouse_pos[1] > self.y:
                # Left arrow
                pygame.draw.polygon(display, background_color_hover,
                                    ((self.x + 25, self.y + self.height), (self.x + 25, self.y),
                                     (self.x, self.y + (self.height / 2)), 25))
                # Text
                Text.render_label(text, color, font_family, font_size, self.x + 80, self.y + (self.height / 2), '',
                                  display)
                # Right arrow
                pygame.draw.polygon(display, background_color,
                                    ((self.x + 135, self.y + self.height), (self.x + 135, self.y),
                                     (self.x + 160, self.y + (self.height / 2)), 25))
            # Above right arrow
            elif self.x + 160 > mouse_pos[0] > self.x + 135 and self.y + self.height > mouse_pos[1] > self.y:
                # Left arrow
                pygame.draw.polygon(display, background_color,
                                    ((self.x + 25, self.y + self.height), (self.x + 25, self.y),
                                     (self.x, self.y + (self.height / 2)), 25))
                # Text
                Text.render_label(text, color, font_family, font_size, self.x + 80, self.y + (self.height / 2), '',
                                  display)
                # Right arrow
                pygame.draw.polygon(display, background_color_hover,
                                    ((self.x + 135, self.y + self.height), (self.x + 135, self.y),
                                     (self.x + 160, self.y + (self.height / 2)), 25))
            else:
                # Left arrow
                pygame.draw.polygon(display, background_color,
                                    ((self.x + 25, self.y + self.height), (self.x + 25, self.y),
                                     (self.x, self.y + (self.height / 2)), 25))
                # Text
                Text.render_label(text, color, font_family, font_size, self.x + 80, self.y + (self.height / 2), '',
                                  display)
                # Right arrow
                pygame.draw.polygon(display, background_color,
                                    ((self.x + 135, self.y + self.height), (self.x + 135, self.y),
                                     (self.x + 160, self.y + (self.height / 2)), 25))

        def mouse_above_left_arrow(self):
            mouse_pos = pygame.mouse.get_pos()
            return self.x + 25 > mouse_pos[0] > self.x and self.y + self.height > mouse_pos[1] > self.y

        def mouse_above_right_arrow(self):
            mouse_pos = pygame.mouse.get_pos()
            return self.x + 160 > mouse_pos[0] > self.x + 135 and self.y + self.height > mouse_pos[1] > self.y

    # Static variables
    fullscreen = False
    volume = 0.50
    timeLimit = 180
    rounds = 3
    controlPlayer1 = Control(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_l, pygame.K_i,
                             pygame.K_o)
    controlPlayer2 = Control(pygame.K_r, pygame.K_f, pygame.K_d, pygame.K_g, pygame.K_x, pygame.K_a, pygame.K_s)

    @staticmethod
    def key_is_repeated(key_code):
        result = False
        if Option.controlPlayer1.moveUp == key_code:
            result = True
        elif Option.controlPlayer1.moveDown == key_code:
            result = True
        elif Option.controlPlayer1.moveLeft == key_code:
            result = True
        elif Option.controlPlayer1.moveRight == key_code:
            result = True
        elif Option.controlPlayer1.jump == key_code:
            result = True
        elif Option.controlPlayer1.primaryBasicAttack == key_code:
            result = True
        elif Option.controlPlayer1.secondaryBasicAttack == key_code:
            result = True
        elif Option.controlPlayer2.moveUp == key_code:
            result = True
        elif Option.controlPlayer2.moveDown == key_code:
            result = True
        elif Option.controlPlayer2.moveLeft == key_code:
            result = True
        elif Option.controlPlayer2.moveRight == key_code:
            result = True
        elif Option.controlPlayer2.jump == key_code:
            result = True
        elif Option.controlPlayer2.primaryBasicAttack == key_code:
            result = True
        elif Option.controlPlayer2.secondaryBasicAttack == key_code:
            result = True
        return result
