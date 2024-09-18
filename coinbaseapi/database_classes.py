class Transaction():
    def __init__(self, transaction_id, type, amount, currency, value, timestamp):
        self.transaction_id = transaction_id
        self.type = type
        self.amount = amount
        self.currency = currency
        self.value = value
        self.timestamp = timestamp

class Holdings():
    def __init__(self, currency, amount, value):
        self.currency = currency
        self.amount = amount
        self.value = value