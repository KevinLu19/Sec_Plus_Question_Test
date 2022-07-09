import sqlite3
import sys


class Questions:
    def __init__(self, DATABASE="questions.db"):
        try:
            self.conn = sqlite3.connect(DATABASE)
        except:
            print("Cannot connect to database.")
            sys.exit()

        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS questions(id INTEGER PRIMARY KEY, question UNIQUE, answer VARCHAR(15))")
    
    def add_entry(self, question, answer):
        
        self.conn.execute("INSERT OR IGNORE INTO questions(question, answer) VALUES (?,?)", (question, answer))
        self.conn.commit()

    def search_table(self, search_question):
        sql_command = f"SELECT * FROM questions where question={search_question}"
        return self.conn.execute(sql_command)

    def print_table(self):
        sql_command = "SELECT question, answer FROM questions"
        self.cur.execute(sql_command)
        items = self.cur.fetchall()

        for item in items:
            for tup in item:
                print(tup)

    def _drop_table(self):
        self.cur.execute("DROP TABLE questions")

if __name__ == "__main__":
    sample_question = """
    1. Which of the following will MOST likely adversely impact the operations of unpatched traditional programmable-logic controllers, running a back-end LAMP server and OT systems with human-management interfaces that are accessible over the Internet via a web interface? (Choose two.)
A. Cross-site scripting
B. Data exfiltration
C. Poor system logging
D. Weak encryption
E. SQL injection
F. Server-side request forgery"""

    sample_question_answer = "Answers: D and F"

    question = Questions()
    question.add_entry(sample_question, sample_question_answer)
    question.print_table()