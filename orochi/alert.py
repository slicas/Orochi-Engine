import pyautogui
import traceback
import tkinter as tk
from tkinter import messagebox
import easygui
import pyperclip



def alert(title,content):
    return(pyautogui.alert(content, title))
def confirm(content):
    return pyautogui.confirm(content)  # returns "OK" or "Cancel"

def prompt(content):
    return pyautogui.prompt(content)  # returns string or None

def password(content):
    return pyautogui.password(content)  # returns string or None


def ERROR(e,traceback,command = ""):
    content = f'{e}\n{traceback}\n{command}'
    pyperclip.copy(f"THIS CONTENT WAS COPIED BY THE OROCHI ERRORS CATCH, WITH THE FOLLOWING ERROR:\n{e}\nWITH THE FOLLOWING TRACEBACK:\n{traceback}\n{command}")
    return easygui.buttonbox(content,"Error",['Exit','Stay'],default_choice="Exit",cancel_choice="Exit")

