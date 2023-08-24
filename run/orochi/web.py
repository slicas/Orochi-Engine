import pyray as pr
import requests
import json 
from orochi.dir import *
cur_dir = CLIENT_DIR



def request_get(url):
    try:
        res = requests.get(url)
        return json.loads(res)
    except:
        return False

def open_url(url):
    pr.open_url(url)

