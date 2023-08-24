import pyautogui
import easygui
import pyperclip



def alert(title,content):
    content = str(content)
    title = str(content)

    return(pyautogui.alert(content, title))
def confirm(content):
    content = str(content)
    return pyautogui.confirm(content)  # returns "OK" or "Cancel"

def prompt(content):
    content = str(content)
    return pyautogui.prompt(content)  # returns string or None

def password(content):
    content = str(content)
    return pyautogui.password(content)  # returns string or None


def ERROR(e,traceback,command = ""):
    content = f'{e}\n{traceback}\n{command}'
    pyperclip.copy(f"THIS CONTENT WAS COPIED BY THE OROCHI ERRORS CATCH, WITH THE FOLLOWING ERROR:\n{e}\nWITH THE FOLLOWING TRACEBACK:\n{traceback}\n{command}")
    return easygui.buttonbox(content,"Error",['Exit','Stay'],default_choice="Exit",cancel_choice="Exit")

