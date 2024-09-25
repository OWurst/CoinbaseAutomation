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
                timestamp DATETIME,
                asset TEXT,
                type TEXT, 
                amount REAL,
                value REAL
            )
        ''')
        c.close()

    def create_holdings_table(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS holdings (
                asset TEXT PRIMARY KEY,
                amount REAL
            )
        ''')
        c.close()

    def store_transaction(self, transaction):
        try:
            conn = sqlite3.connect(self.db_filename)
            c = conn.cursor()
            c.execute('''
                INSERT INTO transactions (transaction_id, timestamp, type, amount, asset, value)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (transaction.transaction_id, transaction.timestamp, transaction.type, transaction.amount, transaction.asset, transaction.value))
            c.close()
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            print("Transaction already exists in database")

    def store_holding(self, holding):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute('''
            INSERT INTO holdings (asset, amount)
            VALUES (?, ?)
            ON CONFLICT(asset) DO UPDATE SET 
                amount = excluded.amount
        ''', (holding.asset, holding.amount))
        c.close()
        conn.commit()
        conn.close()

    def store_historical_resource_ownership(self, historical_resource_ownership):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute('''
            INSERT INTO test_account_values (value, time, asset, amount)
            VALUES (?, ?, ?, ?)
        ''', (historical_resource_ownership.value, historical_resource_ownership.timestamp, historical_resource_ownership.asset, historical_resource_ownership.amount))
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