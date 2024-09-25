from coinbase.rest import RESTClient
import yaml
import ccxt
import sqlite3
import coinbaseapi.database_interface as dbi

# constants
CONFIG_FILENAME = 'coinbase-api-config.yaml'

class CoinbaseApiService:
    def __init__(self):
        # read yaml config file
        with open(CONFIG_FILENAME, 'r') as file:
            config = yaml.safe_load(file)

            key_id = config['apikey-id']
            org_id = config['org-id']

            self.api_key = 'organizations/{org_id}/apiKeys/{key_id}'.format(org_id=org_id, key_id=key_id)
            self.api_secret = config['privkey']

            self.default_currency = config['default-currency']

            self.exchange = ccxt.coinbaseadvanced()

            self.client = RESTClient(api_key=self.api_key, api_secret=self.api_secret)

            self.init_db()
            
    def init_db(self):
        file = "coinbaseapi/trading.db"
        self.db_interface = dbi.DatabaseInterface(file)

    def get_accounts(self):
        return self.client.get_accounts()
    
    def buy_crypto(self, amount, currency, orderId=""):
        quote_size = str(amount)
        product_id = currency + '-' + self.default_currency

        order = self.client.market_order_buy(client_order_id=orderId, product_id=product_id, quote_size=quote_size)
        return order

    def sell_crypto(self, amount, currency, orderId=""):
        quote_size = str(amount)
        product_id = currency + '-' + self.default_currency

        order = self.client.market_order_sell(client_order_id=orderId, product_id=product_id, quote_size=quote_size)
        return order
    
    def get_candles(self, currency, granularity=60, start=None, end=None):
        pass

    def get_order(self, orderId):
        return self.client.get_order(orderId)

    def save_transaction(self, order):
        self.db_interface.store_transaction(order)

    def save_holding(self, holding):
        self.db_interface.store_holding(holding)

    def get_orders(self, status=None, currency=None, start=None, end=None):
        # fetch orders from database based on provided params, else return all orders
        pass
    
    def get_holdings(self):
        # fetch holdings from coinbase
        pass