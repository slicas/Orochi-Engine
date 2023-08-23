import pyray as pr
import webview
from git import Repo
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
    
def clone_git_repo(url, dest):
    try:
        Repo.clone_from(url, dest)
        return True
    except Exception as e:
        print(f"Error on clone repo: {e}")
        return False

def open_url(url):
    pr.open_url(url)


def web_view(title,file):
    webview.create_window(title,CLIENT_DIR+file)
    webview.start()