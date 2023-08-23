import pyray as pr
from orochi.utils import *
from orochi.math import point_direction
MB_LEFT = pr.MouseButton.MOUSE_BUTTON_LEFT
MB_RIGHT = pr.MouseButton.MOUSE_BUTTON_RIGHT
MB_MIDDLE = pr.MouseButton.MOUSE_BUTTON_MIDDLE

INPUT_CURSOR = pr.MouseCursor.MOUSE_CURSOR_IBEAM
RESIZE_CURSOR = pr.MouseCursor.MOUSE_CURSOR_RESIZE_ALL
NOT_CURSOR = pr.MouseCursor.MOUSE_CURSOR_NOT_ALLOWED
POINTER_CURSOR = pr.MouseCursor.MOUSE_CURSOR_POINTING_HAND
CROSSHAIR_CURSOR = pr.MouseCursor.MOUSE_CURSOR_CROSSHAIR
DEFAULT_CURSOR = pr.MouseCursor.MOUSE_CURSOR_DEFAULT


def change_cursor(cursor):
    pr.set_mouse_cursor(cursor)
def get_gui_mouse_position():
    return pr.get_mouse_x(),pr.get_mouse_y()

def get_gui_mouse_x():
    return pr.get_mouse_x()

def get_gui_mouse_y():
    return pr.get_mouse_y()

def point_to_mouse(object,game,corr = 0):
    return point_direction(object.x, object.y, get_world_mouse_x(game), get_world_mouse_y(game)) + corr

def get_world_mouse_x(game):
    return get_relative_to_world_value((pr.get_mouse_x(),0),game)[0]

def get_world_mouse_y(game):
    return get_relative_to_world_value((0,pr.get_mouse_y()),game)[1]


def is_mouse_button_down(button):
    return pr.is_mouse_button_down(button)

def is_mouse_button_pressed(button):
    return pr.is_mouse_button_pressed(button)

def is_mouse_button_released(button):
    return pr.is_mouse_button_released(button)

def is_mouse_button_up(button):
    return pr.is_mouse_button_up(button)
def wheel_move():
    return pr.get_mouse_wheel_move()


