import sqlite3
import unittest

# import src.database as live_database_code
from src import database as live_database_code

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
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute("CREATE TABLE IF NOT EXIST test(id INTEGER, question TEXT, answer TEXT, explaination TEXT)")
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO test('{question}', '{answer}')")

    def test_print_table(self):
        live_database_class = live_database_code.Questions()
        print(live_database_class.print_table())
        return self.cur.execute("SELECT * FROM test")

def main():
    unittest.main()

if __name__ == "__main__":
    main()