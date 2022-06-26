import sqlite3
import sys

class Questions:
    def __init__(self, DATABASE="questions.db"):
        try:
            self.cursor = sqlite3.connect(DATABASE)
        except:
            print("Cannot connect to database.")
            sys.exit()

        self.cursor = DATABASE.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS question(id INTEGER, question TEXT, answer TEXT, explaination TEXT)")
    
    def add_entry(self, entry):
        
        if len(entry) < 0:
            print("Invalid entry.") 
            sys.exit()

    def print_table(self):
        return self.cursor.execute("SELECT * FROM question")