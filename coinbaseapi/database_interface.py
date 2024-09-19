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

    def store_transaction(self, transaction):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute('''
            INSERT INTO transactions (type, amount, asset, value, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (transaction.type, transaction.amount, transaction.asset, transaction.value, transaction.timestamp))
        c.close()
        conn.commit()
        conn.close()

    def store_holding(self, holding):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute('''
            INSERT INTO holdings (asset, amount, value)
            VALUES (?, ?, ?)
            ON CONFLICT(asset) DO UPDATE SET 
                amount = excluded.amount,
                value = excluded.value
        ''', (holding.asset, holding.amount, holding.value))
        c.close()
        conn.commit()
        conn.close()
    
    def get_transactions(self):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute('''
            SELECT * FROM transactions
        ''')
        transactions = c.fetchall()
        c.close()
        conn.close()

        return transactions
    
    def get_holdings(self):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute('''
            SELECT * FROM holdings
        ''')
        holdings = c.fetchall()
        c.close()
        conn.close()

        return holdings
    
    def get_transactions_by_asset(self, asset):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute('''
            SELECT * FROM transactions WHERE asset = ?
        ''', (asset,))
        transactions = c.fetchall()
        c.close()
        conn.close()

        return transactions
    
    def get_holdings_by_asset(self, asset):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute('''
            SELECT * FROM holdings WHERE asset = ?
        ''', (asset,))
        holdings = c.fetchall()
        c.close()
        conn.close()

        return holdings