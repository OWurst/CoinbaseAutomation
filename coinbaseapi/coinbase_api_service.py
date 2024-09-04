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

            api_key = 'organizations/{org_id}/apiKeys{key_id}'.format(org_id=org_id, key_id=key_id)
            secret_key_filename = config['privkey-filename']

            api_secret = read_pem(secret_key_filename)

            self.client = RESTClient(api_key=api_key, api_secret=api_secret)

    def get_accounts(self):
        return self.client.get_accounts()

def read_pem(filename):
    with open(filename, 'r') as file:
        secret_key = file.read()
        return secret_key    