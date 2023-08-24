import subprocess
from orochi.dir import *
import orochi.object
import threading
import psutil


cur_dir = CLIENT_DIR
process = psutil.Process()
memory_info = process.memory_info()

class Thread:
    def __init__(self,game,function):
        self.game = game
        self.function = function
        self.thread = threading.Thread(target=self.function, args=(self,self.game,))
        self.active = False
        self.values = []
        self.profile = orochi.object.Profile()
    def store(self,value):
        self.values.append(value)
    def execute(self):
        self.thread.start()

def python_subprocess(file):
    process = subprocess.Popen(["python", cur_dir+file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    exit_msg, error = process.communicate()
    exit_msg = exit_msg.decode("utf-8")
    error = error.decode("utf-8")
    return exit_msg,error

def get_memory_usage(bytes = False):
    return psutil._common.bytes2human(memory_info.rss) if not bytes else memory_info.rss
def get_cpu_usage():
    return psutil.cpu_percent()


def windows_cmd_command_execute(command,keep = False):
    keep = "/c" if not keep else "/k"
    subprocess.run(["cmd", keep,command])

