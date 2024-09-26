import sqlite3
import pandas as pd
import ccxt

class BasicTrainingDB:
    def __init__(self):
        self.conn = sqlite3.connect('training_data.db')
        self.conn.close()
        
        self.exchange = ccxt.coinbaseadvanced()