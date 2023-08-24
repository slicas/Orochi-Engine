import pyray as pr

letters = {
    "0": 48,
    "1": 49,
    "2": 50,
    "3": 51,
    "4": 52,
    "5": 53,
    "6": 54,
    "7": 55,
    "8": 56,
    "9": 57,
    "a": 65,
    "b": 66,
    "c": 67,
    "d": 68,
    "e": 69,
    "f": 70,
    "g": 71,
    "h": 72,
    "i": 73,
    "j": 74,
    "k": 75,
    "l": 76,
    "m": 77,
    "n": 78,
    "o": 79,
    "p": 80,
    "q": 81,
    "r": 82,
    "s": 83,
    "t": 84,
    "u": 85,
    "v": 86,
    "w": 87,
    "x": 88,
    "y": 89,
    "z": 90,
}
keys = {
    "0": 48,
    "1": 49,
    "2": 50,
    "3": 51,
    "4": 52,
    "5": 53,
    "6": 54,
    "7": 55,
    "8": 56,
    "9": 57,
    "backspace": pr.KeyboardKey.KEY_BACKSPACE,
    "tab": 9,
    "enter": 13,
    "shift": 16,
    "ctrl": 17,
    "alt": 18,
    "pausebreak": 19,
    "capslock": 20,
    "esc": 27,
    "space": 32,
    "pageup": 33,
    "pagedown": 34,
    "end": 35,
    "home": 36,
    "left": 263,
    "up": 265,
    "right": 262,
    "down": 264,
    "print_screen":44,
    "insert": 45,
    "delete": 46,
    "a": 65,
    "b": 66,
    "c": 67,
    "d": 68,
    "e": 69,
    "f": 70,
    "g": 71,
    "h": 72,
    "i": 73,
    "j": 74,
    "k": 75,
    "l": 76,
    "m": 77,
    "n": 78,
    "o": 79,
    "p": 80,
    "q": 81,
    "r": 82,
    "s": 83,
    "t": 84,
    "u": 85,
    "v": 86,
    "w": 87,
    "x": 88,
    "y": 89,
    "z": 90,
    "leftwindowkey": 91,
    "rightwindowkey": 92,
    "selectkey": 93,
    "numpad0": 96,
    "numpad1": 97,
    "numpad2": 98,
    "numpad3": 99,
    "numpad4": 100,
    "numpad5": 101,
    "numpad6": 102,
    "numpad7": 103,
    "numpad8": 104,
    "numpad9": 105,
    "multiply": 106,
    "add": 107,
    "subtract": 109,
    "decimalpoint": 110,
    "divide": 111,
    "f1": 112,
    "f2": 113,
    "f3": 114,
    "f4": 115,
    "f5": 116,
    "f6": 117,
    "f7": 118,
    "f8": 119,
    "f9": 120,
    "f10": 121,
    "f11": 122,
    "f12": 123,
    "numlock": 144,
    "scrolllock": 145,
    "semicolon": 186,
    "equalsign": 187,
    "comma": 188,
    "dash": 189,
    "period": 190,
    "forwardslash": 191,
    "graveaccent": 192,
    "openbracket": 219,
    "backslash": 220,
    "closebracket": 221,
    "singlequote": 222
}

def user_write():
    for key, value in letters.items():
        if pr.is_key_pressed(value):
            return key
    return False

def is_any_key_down():
    for key in range(48, 222):
        if pr.is_key_down(key):
            return True
    return False

def get_downed_key():
    for key, value in keys.items():
        if pr.is_key_down(value):
            return key
    return False

def get_pressed_key():
    for key, value in keys.items():
        if pr.is_key_pressed(value):
            return key
    return False

def get_pressed_released():
    for key, value in keys.items():
        if pr.is_key_released(value):
            return key
    return False

def key_down(key):
        return pr.is_key_down(keys[key])
def key_pressed(key):
        return pr.is_key_pressed(keys[key])
def key_released(key):
        return pr.is_key_released(keys[key])
def key_up(key):
        return pr.is_key_up(keys[key])


