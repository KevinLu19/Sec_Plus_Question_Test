import sqlite3
import unittest
import sys
import pprint

question = """1. Which of the following will MOST likely adversely impact the operations of unpatched traditional programmable-logic controllers, running a back-end LAMP server and OT systems with human-management interfaces that are accessible over the Internet via a web interface? (Choose two.)

A. Cross-site scripting

B. Data exfiltration

C. Poor system logging

D. Weak encryption

E. SQL injection

F. Server-side request forgery"""

answer = "D and F"

class TestDatabase(unittest.TestCase):
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

    def test_add_entry(self, question, answer):
        duplicate_search = self.test_search_table(question)
        
        if not duplicate_search:     
            self.conn.execute("INSERT INTO test(question, answer) VALUES (?,?)", (question, answer))
            self.conn.commit()
        else:
            print("Already exists in the table.")

    def test_query_table(self, question):
        sql_command = f"SELECT * FROM test WHERE question={question}"
        return self.conn.execute(sql_command)

    def test_query_table_entry(self):
        pass

    def test_query_question_column(self):
        pass

    def test_check_for_duplicate(self):
        pass

    def test_update_table_entry(self):
        pass

    def test_print_table(self):
        self.cur.execute("SELECT * FROM test")
        items = self.cur.fetchall()

        for item in items:
            print(item)
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()