import sqlite3
from .database_conection import database_connection


def create_book_table() -> str:
    with database_connection('data.db') as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)')


def add_books(name: str, author: str) -> str:
    with database_connection('data.db') as cursor:
        cursor.execute('INSERT INTO books VALUES(?,?,0)', (name, author))


def get_all_books() -> str:
    with database_connection('data.db') as cursor:

        cursor.execute('SELECT * FROM books')
        # list of tupples
        books = [{'name': row[0], 'author': row[1], 'read': row[2]}
                 for row in cursor.fetchall()]
        return books


def mark_book_as_read(name: str):
    with database_connection('data.db') as cursor:
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name))


def delete_book(name: str):
    with database_connection('data.db') as cursor:
        cursor.execute('DELETE FROM books WHERE name=?', (name))
