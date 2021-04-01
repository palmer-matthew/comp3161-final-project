from mysql import connector
import mysql.connector as db
from mysql.connector import Error

def connect():
    try:
        conn = None
        conn = db.connect(host='localhost', database='planner', user='root', password='')
    except Error as e:
        print(f'Log: Error {e.msg}')
        conn = None
    return conn

def close(connection):
    connection.close()

def executeQuery(query, connection):
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(query)
    except Error as e:
        print(f'Log: Error {e.msg}')
        return None
    return 'OK'



