from coinbase.rest import RESTClient
import yaml
import ccxt

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
    
    def get_candles(self, currency, start, end, granularity):
        pass
    