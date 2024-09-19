import sqlite3

from coinbaseapi.coinbase_api_service import CoinbaseApiService
import coinbaseapi.database_interface as dbi

# class extends coinbase_api_service
class CoinbaseApiPaperTradingService(CoinbaseApiService):
    def init_db(self):
        file = "coinbaseapi/paper_trading.db"
        self.db_interface = dbi.DatabaseInterface(file)

        conn = sqlite3.connect(file)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS test_account_values (
                value REAL,
                time DATETIME
            )
        ''')
        c.close()
        conn.commit()
        conn.close()

    def buy_crypto(self, amount, currency, orderId=""):
        print("Paper trading: buy_crypto")
        return None
    
    def sell_crypto(self, amount, currency, orderId=""):
        print("Paper trading: sell_crypto")
        return None
    
    def get_holdings(self):
        print("Paper trading: get_holdings")
        return None
class TestAccountValue():
    def __init__(self, value, time):
        self.value = value
        self.time = time