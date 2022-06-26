import sqlite3
import sys
import unittest

class Questions:
    def __init__(self, DATABASE="questions.db"):
        try:
            self.cursor = sqlite3.connect(DATABASE)
        except:
            print("Cannot connect to database.")
            sys.exit()

        self.cursor = DATABASE.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS question(id INTEGER, question TEXT, answer TEXT)")
    
    def add_entry(self, cursor, entry):
        pass

