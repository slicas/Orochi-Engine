import sqlite3 as sq
from orochi.alert import ERROR
import traceback
from orochi.dir import CLIENT_DIR
cur_dir = CLIENT_DIR + "/src/"
class Database:
    def __init__(self,name):
        self.name = name
        self.conn = sq.connect(f"{cur_dir}{self.name}.db")
        self.report_error = True
    def drop(self,table):
        command = f'''
                DROP TABLE IF EXISTS {table.name} 
                '''
        def func():
            cursor = self.conn.cursor()
            cursor.execute(command)
            self.conn.commit()
            cursor.close()
        try:
          return func()
        except Exception as e:
            if(self.report_error):
                ERROR(e,traceback.format_exc(),command)
            return False

class Table:
    def __init__(self,name):
        self.name = name
    def create(self,database : Database,keys : str):
        command = f'''
                CREATE TABLE IF NOT EXISTS {self.name}(
                "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                {keys})
                '''
        def func():
            cursor = database.conn.cursor()
            cursor.execute(command)
            database.conn.commit()
            cursor.close()
            return True
        
        try:
            return func()
        except Exception as e:
            if(database.report_error):
                ERROR(e,traceback.format_exc(),command)
            return False

    def add(self,database : Database,keys : str,values : str):
        command = f'''
                INSERT INTO {self.name} ({keys}) VALUES ({values})
                '''
        def func():
            
            cursor = database.conn.cursor()
            
            cursor.execute(command)
            database.conn.commit()
            cursor.close()
            return True
        try:
            return func()
        except Exception as e:
            if(database.report_error):
                ERROR(e,traceback.format_exc(),command)
            return False
    def edit(self,database : Database,args : str,keys : str):
        command = f'''
                UPDATE {self.name} SET {keys} {args}
                '''
        def func():
            cursor = database.conn.cursor()
            
            cursor.execute(command)
            database.conn.commit()
            cursor.close()
            return True
        try:
            return func()
        except Exception as e:
            if(database.report_error):
                ERROR(e,traceback.format_exc(),command)
            return False
    def search(self,database : Database,keys : str,args : str):
        command = f'''
                SELECT {keys} FROM {self.name} {args}
                '''
        def func():
            cursor = database.conn.cursor()
            
            cursor.execute(command)
            return cursor.fetchall()
        try:
            return func()
        except Exception as e:
            if(database.report_error):
                ERROR(e,traceback.format_exc(),command)
            return False
    def delete(self,database : Database,args : str):
        command = f'''
                DELETE FROM {self.name} {args}
                '''
        def func():
            cursor = database.conn.cursor()
            
            cursor.execute(command)
            database.conn.commit()
            cursor.close()
            return True
        try:
            return func()
        except Exception as e:
            if(database.report_error):
                ERROR(e,traceback.format_exc(),command)
            return False
       
    