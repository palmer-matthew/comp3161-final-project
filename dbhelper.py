import mysql.connector as db
from mysql.connector import Error
import os

#cursor methods: fetchone() , fetchmany() , and fetchall()

def connect(database=None):
    try:
        conn = None
        if database == None:
            conn = db.connect(host='localhost', user='root', password= '')
        else:
            conn = db.connect(host='localhost', database='planner', user='root', password='')
    except Error as e:
        print(f'Log: Error {e.msg}')
        conn = None
    return conn

def close(connection):
    connection.close()

def executeNQuery(query, connection, m=False):
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(query, multi=m)
        connection.commit()
        cursor.close()
    except Error as e:
        connection.rollback()
        print(f'Log: Error {e.msg}')
        return None
    return 'OK'

def executeRQuery(query, connection, m=False):
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.execute(query, multi=m)
        results = cursor.fetchall()
        return results
    except Error as e:
        connection.rollback()
        print(f'Log: Error {e.msg}')
        return None

def executeProcedure(procedure, args, connection):
    try:
        cursor = None
        cursor = connection.cursor()
        cursor.callproc(procedure, args)
        results  = cursor.stored_results()
        return results
    except Error as e:
        connection.rollback()
        print(f'Log: Error {e.msg}')
        return None
