# class extends coinbase_api_service

from coinbaseapi.coinbase_api_service import CoinbaseAPIService

class CoinbaseAPIServicePaperTrading(CoinbaseAPIService):
    def buy_crypto(self, amount, currency, orderId=""):
        print("Paper trading: buy_crypto")
        return None
    
    def sell_crypto(self, amount, currency, orderId=""):
        print("Paper trading: sell_crypto")
        return None