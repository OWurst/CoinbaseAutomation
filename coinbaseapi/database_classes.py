import datetime

class Transaction():
    def __init__(self, transaction_id=0, type=None, amount=0, asset=None, value=0, timestamp=datetime.datetime.now()):
        self.transaction_id = transaction_id
        self.type = type
        self.amount = amount
        self.asset = asset
        self.value = value
        self.timestamp = timestamp

    def __str__(self):
        return "Transaction ID: {transaction_id}, Type: {type}, Amount: {amount}, Asset: {asset}, Value: {value}, Timestamp: {timestamp}".format(transaction_id=self.transaction_id, type=self.type, amount=self.amount, asset=self.asset, value=self.value, timestamp=self.timestamp)

class Holding():
    def __init__(self, asset="unknown", amount=0, value=0):
        self.asset = asset
        self.amount = amount
        self.value = value

    def __str__(self):
        return "Asset: {asset}, Amount: {amount}, Value: {value}".format(asset=self.asset, amount=self.amount, value=self.value)
    