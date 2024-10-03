import sqlite3
import basic_training_db as base
import pandas as pd

class SimpleCandleDB(base.BasicTrainingDB):
    def create_table(self, timeframe = '1h'):
        self.timeframe = timeframe
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
        '''.format(timeframe=timeframe))
        self.conn.commit()
        self.conn.close()

    def insert_candle(self, candle):
        id = candle['asset'] + '_' + candle['timestamp']
        asset = candle['asset']
        timestamp = candle['timestamp']
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
        # insert whole df into db
        df['candle_id'] = df['asset'] + '_' + df['timestamp']

        self.conn = sqlite3.connect('training_data.db')
        df.to_sql('candles_{timeframe}'.format(timeframe=self.timeframe), self.conn, if_exists='append', index=False)       

        self.conn.commit()
        self.conn.close()


    def create_candles(self, asset='BTC', timeframe='1h', start=None):
        if start is None:
            # get candles for the last 30 days
            start = self.exchange.milliseconds() - 30 * 86400 * 1000

        symbol = asset + '/USDC'
        limit = 30*24

        candles = self.exchange.fetch_ohlcv(symbol, timeframe, start, limit)

        df = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['asset'] = asset
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')

        return df

