import json
import tempfile
import os
from orochi.game import *

from orochi.dir import *
import promptlib
import configparser
from orochi.os import *
json = json
cur_dir = CLIENT_DIR
cur_dir += "/src/"
temp_dir = tempfile.gettempdir()






def get_folder():
    prompter = promptlib.Files()
    folder = prompter.dir()
    return folder
def get_file():
    prompter = promptlib.Files()
    file = prompter.file()
    return file

def file_exist(src,temp = False):
    file = f"{cur_dir}/{src}" if not temp else f"{temp_dir}/{src}"
    return os.path.isfile(file)

def write_json(filename,content,temp = False):
    filename = f"{cur_dir}/{filename}.json" if not temp else f"{temp_dir}/{filename}.json"
    with open(filename,"w") as out:
        out.write(content)
        return True

def read_json(filename,temp = False):
    filename = f"{cur_dir}/{filename}.json" if not temp else f"{temp_dir}/{filename}.json"
    with open(filename,"r") as out:
        return json.load(out)
    
def json_to_string(data):
    return json.dumps(data)
def string_to_json(data):
    return json.loads(data)

def create_ini(filename, temp=False):
    file_path = os.path.join(temp_dir if temp else cur_dir, f"{filename}.ini")
    config = configparser.ConfigParser()
    with open(file_path, 'w') as file:
        config.write(file)

def add_key(filename, section, key, value, temp=False):
    file_path = os.path.join(temp_dir if temp else cur_dir, f"{filename}.ini")
    config = configparser.ConfigParser()
    config.read(file_path)
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, key, value)

    with open(file_path, 'w') as file:
        config.write(file)

def edit_key(filename, section, key, new_value, temp=False):
    file_path = os.path.join(temp_dir if temp else cur_dir, f"{filename}.ini")
    config = configparser.ConfigParser()
    config.read(file_path)
    if not config.has_section(section) or not config.has_option(section, key):
        print("Key not found.")
        return
    config.set(section, key, new_value)

    with open(file_path, 'w') as file:
        config.write(file)

def get_key(filename, section, key, temp=False):
    file_path = os.path.join(temp_dir if temp else cur_dir, f"{filename}.ini")
    config = configparser.ConfigParser()
    config.read(file_path)
    if config.has_section(section) and config.has_option(section, key):
        return config.get(section, key)
    return None

def get_all_keys(filename, temp=False):
    file_path = os.path.join(temp_dir if temp else cur_dir, f"{filename}.ini")
    config = configparser.ConfigParser()
    config.read(file_path)
    keys = {}

    for section in config.sections():
        keys[section] = dict(config.items(section))

    return keys

class Listener:
    def __init__(self,game,ID):
        self.__game = game
        self.__keys = {}
        self.__ID = ID
        self.__values = {}
    def add_key(self,ID,value = ""):
        self.__keys[ID] = value
        return value
    def init(self):
        self.__game.awalys_on_top()
        write_json(self.__ID,json_to_string(self.__keys))
        windows_cmd_command_execute(f"{cur_dir}{self.__ID}.json")
    def update(self):
        self.__values = read_json(self.__ID)
    def listen(self,ID):
        try:
            return self.__values[ID]
        except Exception as e:
            print(self.__values,f"\nError on: {e}")
            return 0