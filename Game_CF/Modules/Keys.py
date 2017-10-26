import pygame


class Key:
    dictionary = {
        pygame.K_BACKSPACE: 'BACKSPACE',
        pygame.K_TAB: 'TAB',
        pygame.K_CLEAR: 'CLEAR',
        pygame.K_RETURN: 'RETURN',
        pygame.K_PAUSE: 'PAUSE',
        pygame.K_ESCAPE: 'ESCAPE',
        pygame.K_SPACE: 'SPACE',
        pygame.K_EXCLAIM: 'EXCLAIM',
        pygame.K_QUOTEDBL: 'QUOTEDBL',
        pygame.K_HASH: 'HASH',
        pygame.K_DOLLAR: 'DOLLAR',
        pygame.K_AMPERSAND: 'AMPERSAND',
        pygame.K_QUOTE: 'QUOTE',
        pygame.K_LEFTPAREN: 'LEFTPAREN',
        pygame.K_RIGHTPAREN: 'RIGHTPAREN',
        pygame.K_ASTERISK: 'ASTERISK',
        pygame.K_PLUS: 'PLUS',
        pygame.K_COMMA: 'COMMA',
        pygame.K_MINUS: 'MINUS',
        pygame.K_PERIOD: 'PERIOD',
        pygame.K_SLASH: 'SLASH',
        pygame.K_0: '0',
        pygame.K_1: '1',
        pygame.K_2: '2',
        pygame.K_3: '3',
        pygame.K_4: '4',
        pygame.K_5: '5',
        pygame.K_6: '6',
        pygame.K_7: '7',
        pygame.K_8: '8',
        pygame.K_9: '9',
        pygame.K_COLON: 'COLON',
        pygame.K_SEMICOLON: 'SEMICOLON',
        pygame.K_LESS: 'LESS',
        pygame.K_EQUALS: 'EQUALS',
        pygame.K_GREATER: 'GREATER',
        pygame.K_QUESTION: 'QUESTION',
        pygame.K_AT: 'AT',
        pygame.K_LEFTBRACKET: 'LEFTBRACKET',
        pygame.K_BACKSLASH: 'BACKSLASH',
        pygame.K_RIGHTBRACKET: 'RIGHTBRACKET',
        pygame.K_CARET: 'CARET',
        pygame.K_UNDERSCORE: 'UNDERSCORE',
        pygame.K_BACKQUOTE: 'BACKQUOTE',
        pygame.K_a: 'a',
        pygame.K_b: 'b',
        pygame.K_c: 'c',
        pygame.K_d: 'd',
        pygame.K_e: 'e',
        pygame.K_f: 'f',
        pygame.K_g: 'g',
        pygame.K_h: 'h',
        pygame.K_i: 'i',
        pygame.K_j: 'j',
        pygame.K_k: 'k',
        pygame.K_l: 'l',
        pygame.K_m: 'm',
        pygame.K_n: 'n',
        pygame.K_o: 'o',
        pygame.K_p: 'p',
        pygame.K_q: 'q',
        pygame.K_r: 'r',
        pygame.K_s: 's',
        pygame.K_t: 't',
        pygame.K_u: 'u',
        pygame.K_v: 'v',
        pygame.K_w: 'w',
        pygame.K_x: 'x',
        pygame.K_y: 'y',
        pygame.K_z: 'z',
        pygame.K_DELETE: 'DELETE',
        pygame.K_KP0: 'KP0',
        pygame.K_KP1: 'KP1',
        pygame.K_KP2: 'KP2',
        pygame.K_KP3: 'KP3',
        pygame.K_KP4: 'KP4',
        pygame.K_KP5: 'KP5',
        pygame.K_KP6: 'KP6',
        pygame.K_KP7: 'KP7',
        pygame.K_KP8: 'KP8',
        pygame.K_KP9: 'KP9',
        pygame.K_KP_PERIOD: 'KP_PERIOD',
        pygame.K_KP_DIVIDE: 'KP_DIVIDE',
        pygame.K_KP_MULTIPLY: 'KP_MULTIPLY',
        pygame.K_KP_MINUS: 'KP_MINUS',
        pygame.K_KP_PLUS: 'KP_PLUS',
        pygame.K_KP_ENTER: 'KP_ENTER',
        pygame.K_KP_EQUALS: 'KP_EQUALS',
        pygame.K_UP: 'UP',
        pygame.K_DOWN: 'DOWN',
        pygame.K_RIGHT: 'RIGHT',
        pygame.K_LEFT: 'LEFT',
        pygame.K_INSERT: 'INSERT',
        pygame.K_HOME: 'HOME',
        pygame.K_END: 'END',
        pygame.K_PAGEUP: 'PAGEUP',
        pygame.K_PAGEDOWN: 'PAGEDOWN',
        pygame.K_F1: 'F1',
        pygame.K_F2: 'F2',
        pygame.K_F3: 'F3',
        pygame.K_F4: 'F4',
        pygame.K_F5: 'F5',
        pygame.K_F6: 'F6',
        pygame.K_F7: 'F7',
        pygame.K_F8: 'F8',
        pygame.K_F9: 'F9',
        pygame.K_F10: 'F10',
        pygame.K_F11: 'F11',
        pygame.K_F12: 'F12',
        pygame.K_F13: 'F13',
        pygame.K_F14: 'F14',
        pygame.K_F15: 'F15',
        pygame.K_NUMLOCK: 'NUMLOCK',
        pygame.K_CAPSLOCK: 'CAPSLOCK',
        pygame.K_SCROLLOCK: 'SCROLLOCK',
        pygame.K_RSHIFT: 'RSHIFT',
        pygame.K_LSHIFT: 'LSHIFT',
        pygame.K_RCTRL: 'RCTRL',
        pygame.K_LCTRL: 'LCTRL',
        pygame.K_RALT: 'RALT',
        pygame.K_LALT: 'LALT',
        pygame.K_RMETA: 'RMETA',
        pygame.K_LMETA: 'LMETA',
        pygame.K_LSUPER: 'LSUPER',
        pygame.K_RSUPER: 'RSUPER',
        pygame.K_MODE: 'MODE',
        pygame.K_HELP: 'HELP',
        pygame.K_PRINT: 'PRINT',
        pygame.K_SYSREQ: 'SYSREQ',
        pygame.K_BREAK: 'BREAK',
        pygame.K_MENU: 'MENU',
        pygame.K_POWER: 'POWER',
        pygame.K_EURO: 'EURO'
    }

    @staticmethod
    def get_key_label(key_code):
        return Key.dictionary[key_code]
