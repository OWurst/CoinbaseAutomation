import sqlite3
import db_classes as dbc

class DatabaseInterface:
    # constructor takes in a database connection
    def __init__(self, conn):
        self.conn = conn

    def create_transactions_table(self):
        pass