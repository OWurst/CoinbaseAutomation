import sqlite3
import coinbaseapi.database_classes as dbc

class DatabaseInterface:
    # constructor takes in a database connection
    def __init__(self, conn):
        self.db_connection = conn

    def create_transactions_table(self):
        pass