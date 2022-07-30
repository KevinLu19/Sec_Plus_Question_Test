import sqlite3
import unittest
import sys
import pprint
import pymongo

#import src.database as live_database_code
# from src import database as live_database_code

question = """1. Which of the following will MOST likely adversely impact the operations of unpatched traditional programmable-logic controllers, running a back-end LAMP server and OT systems with human-management interfaces that are accessible over the Internet via a web interface? (Choose two.)

A. Cross-site scripting

B. Data exfiltration

C. Poor system logging

D. Weak encryption

E. SQL injection

F. Server-side request forgery"""

answer = "D and F"

class TestSQL(unittest.TestCase):
    def setUp(self) -> None:
        try:
            self.conn = sqlite3.connect(":memory:")
        except:
            print("Database on Memory failed.")
            sys.exit()

        self.conn.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, question UNIQUE, answer VARCHAR(15))")
        self.cur = self.conn.cursor()
        self.test_add(question, answer)
        self.test_print_table()

    def test_add(self, question, answer):
        duplicate_search = self.test_search_table(question)
        
        if not duplicate_search:     
            self.conn.execute("INSERT INTO test(question, answer) VALUES (?,?)", (question, answer))
            self.conn.commit()
        else:
            print("Already exists in the table.")

    def test_search_table(self, question):
        sql_command = f"SELECT * FROM test WHERE question={question}"
        return self.conn.execute(sql_command)

    def test_print_table(self):
        # live_database_class = live_database_code.Questions()
        # print(live_database_class.print_table())
        # return self.cur.execute("SELECT * FROM test")
        self.cur.execute("SELECT * FROM test")
        items = self.cur.fetchall()

        for item in items:
            print(item)
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()