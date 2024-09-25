import sqlite3

from coinbaseapi.coinbase_api_service import CoinbaseApiService
import coinbaseapi.database_interface as dbi
import datetime

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
                time DATETIME,
                asset TEXT,
                amount REAL
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
    
    def save_historical_resource_ownership(self, historical_resource_ownership):
        self.db_interface.store_historical_resource_ownership(historical_resource_ownership)

class HistoricalResourceOwnership():
    def __init__(self, asset=None, amount=0, value=0, timestamp=datetime.datetime.now()):
        self.asset = asset
        self.amount = amount
        self.value = value
        self.timestamp = timestamp

    def __str__(self):
        return "Asset: {asset}, Amount: {amount}, Value: {value}, Timestamp: {timestamp}".format(asset=self.asset, amount=self.amount, value=self.value, timestamp=self.timestamp)
    