from coinbase.rest import RESTClient
import yaml

# constants
CONFIG_FILENAME = 'coinbase-api-config.yaml'
CLIENT_TIMEOUT_SECONDS = 'undefined'

class CoinbaseApiService:
    def __init__(self):
        # read yaml config file
        with open(CONFIG_FILENAME, 'r') as file:
            config = yaml.safe_load(file)

            key_id = config['apikey-id']
            org_id = config['org-id']

            self.api_key = 'organizations/{org_id}/apiKeys{key_id}'.format(org_id=org_id, key_id=key_id)
            self.api_secret = config['privkey']

            self.client = RESTClient(api_key=self.api_key, api_secret=self.api_secret)

    def get_accounts(self):
        return self.client.get_accounts()
    
    def create_portfolio(self, name):
        return self.client.create_portfolio(name=name)