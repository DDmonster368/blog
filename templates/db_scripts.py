import sqlite3

connectioin = None
cursor = None

def open():
    global connectioin,cursor
    connectioin = sqlite3.connect("blog.db")
    cursor = connectioin.cursor()

def close():
    cursor.close()
    connectioin.close()