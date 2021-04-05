import mysql.connector as db
from mysql.connector import Error

#cursor methods: fetchone() , fetchmany() , and fetchall()

def connect(database=None):
    try:
        conn = None
        if database == None:
            conn = db.connect(host='localhost', user='imani', password= '')
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

def executeRQuery(query, connection):
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f'Log: Error {e.msg}')
        return None




