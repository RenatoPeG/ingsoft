import sqlite3
from sqlite3 import Error
from Cholo_Fighter.Fisicas import *


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_connection():
    database = "C:\\Users\Renato\Documents\choloFighter\server\db.sqlite3"
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM menu_personaje')

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_personajes(conn):
    personajes = []
    cur = conn.cursor()
    cur.execute('SELECT * FROM menu_personaje')

    rows = cur.fetchall()

    for row in rows:
        nombre = row[1]
        vida = row[2]
        icono = row[3]
        personaje = Personaje(nombre, '', vida)
        personajes.append(personaje)

    return personajes


def main():
    database = "C:\\Users\Renato\Documents\choloFighter\server\db.sqlite3"

    conn = create_connection(database)
    with conn:
        print("1. Query all tasks")
        select_all_tasks(conn)


if __name__ == '__main__':
    main()
