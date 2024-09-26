import sqlite3
import basic_training_db as base
import pandas as pd

class SimpleCandleDB(base.BasicTrainingDB):
    def create_table(self, timeframe = '1h'):
        self.conn = sqlite3.connect('training_data.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS candles_{timeframe}(
                candle_id TEXT PRIMARY KEY,
                asset TEXT,
                timestamp DATETIME,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                volume REAL
            )
        '''.format(timeframe=self.timeframe))
        self.conn.commit()
        self.conn.close()

    def insert_candle(self, asset, timestamp, candle):
        id = asset + '_' + timestamp
        high = candle['high']
        low = candle['low']
        open = candle['open']
        close = candle['close']
        volume = candle['volume']

        self.conn = sqlite3.connect('training_data.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO candles_{timeframe} VALUES (?, ?, ?, ?, ?, ?, ?, ?)".format(timeframe=self.timeframe), (id, asset, timestamp, open, high, low, close, volume))
        self.conn.commit()
        self.conn.close()

    def insert_candles(self, df):
        for i in range(len(df)):
            self.insert_candle(df.iloc[i])