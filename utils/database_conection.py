import sqlite3
from contextlib import contextmanager

# class DatabaseConnection:

#     def __init__(self, host):
#         self.connection = None
#         self.host = host

#     def __enter__(self):
#         self.conection = sqlite3.connect(self.host)
#         return self.conection

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type or exc_val or exc_tb:
#             self.conection.close()
#         else:
#             self.conection.commit()
#             # self.connection.close()


@contextmanager
def database_connection(destinaton: str):
    connection = sqlite3.connect(destinaton)
    try:
        cursor = connection.cursor()
        yield cursor
    finally:
        connection.commit()
        connection.close()
