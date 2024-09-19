# class extends coinbase_api_service

from coinbaseapi.coinbase_api_service import CoinbaseApiService
import coinbaseapi.database_interface as dbi

class CoinbaseAPIServicePaperTrading(CoinbaseApiService):
    def buy_crypto(self, amount, currency, orderId=""):
        print("Paper trading: buy_crypto")
        return None
    
    def sell_crypto(self, amount, currency, orderId=""):
        print("Paper trading: sell_crypto")
        return None
    
    def get_holdings(self):
        print("Paper trading: get_holdings")
        return None
    
    def init_db(self):
        print("Paper trading: init_db")
        return None
    
class TestAccountValue():
    def __init__(self, value, time):
        self.value = value
        self.time = time