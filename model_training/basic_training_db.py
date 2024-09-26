import sqlite3
import pandas as pd

class BasicTrainingDB:
    def __init__(self):
        self.conn = sqlite3.connect('training_data.db')
        self.conn.close()
        