import sqlite3
import coinbaseapi.database_classes as dbc

class DatabaseInterface:
    # constructor takes in a database connection
    def __init__(self, file):
        self.db_filename = file
        self.conn = sqlite3.connect(self.db_filename)

        # create tables
        self.create_transactions_table()
        self.create_holdings_table()

        # kill the connection
        self.conn.commit()
        self.conn.close()

    def create_transactions_table(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY,
                type TEXT, amount REAL,
                asset TEXT,
                value REAL,
                timestamp DATETIME
            )
        ''')
        c.close()

    def create_holdings_table(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS holdings (
                asset TEXT PRIMARY KEY,
                amount REAL,
                value REAL
            )
        ''')
        c.close()