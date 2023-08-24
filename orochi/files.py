import json
import tempfile
import os
from dir import *
import configparser
json = json
cur_dir = CLIENT_DIR
temp_dir = tempfile.gettempdir()

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
    
def to_json(data):
    return json.dumps(data)

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

