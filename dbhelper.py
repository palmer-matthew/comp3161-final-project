from mysql import connector
import mysql.connector as db
from mysql.connector import Error

def connect(database=None):
    try:
        conn = None
        if database == None:
            conn = db.connect(host='localhost', user='root', password='')
        else:
            conn = db.connect(host='localhost', database='planner', user='root', password='')
    except Error as e:
        print(f'Log: Error {e.msg}')
        conn = None
    return conn

def close(connection):
    connection.close()

def executeNQuery(query, connection):
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
    except Error as e:
        print(f'Log: Error {e.msg}')
        return None
    return 'OK'



