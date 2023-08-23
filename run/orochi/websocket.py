import websocket
import threading
import json as js
import sys
from orochi.files import *
class WebSocket():
    def __init__(self,game,ip,on_message,on_error = None,on_open = None,on_close = None):
        self.game = game
        self.ip = ip
        self.websocket = websocket
        self.ws = None
        self.__connection_status = "Offline"
        self.__on_message = on_message
        self.__on_error = on_error
        self.__on_open = on_open           
        self.__on_close = on_close             
        
    def get_connection_status(self):
        return self.__connection_status
    def connect(self):
        def on_message(ws,message):
            try:
                self.__on_message(ws,message)
            except Exception as e:
                    return e
        def on_close(ws, close_status_code, close_msg):
            self.__connection_status = "Offline"
            if(self.__on_close):
                self.__on_close(ws, close_status_code, close_msg)
        def on_error(ws,error):
            print("error")
            if(self.__on_error):
                    self.__on_error(ws,error)
        def on_open(ws):
            self.__connection_status = "Online"
            if(self.__on_open):
                self.__on_open(ws)
        def connection():
            self.ws = self.websocket.WebSocketApp(f"{self.ip}",on_open=on_open,on_close=on_close,on_error=on_error, on_message=on_message )
            self.game.ws_conn = self.ws
            self.ws.run_forever()
            
        
        websocket_thread = threading.Thread(target=connection)
        websocket_thread.start()
    def send_message(self,message):
        if(self.__connection_status == "Online"):
            try:
                message = self.ws.send(message)
                return True
            except Exception as e:
                return e
        else:
            return False
