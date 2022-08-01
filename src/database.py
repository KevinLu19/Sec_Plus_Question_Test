import sqlite3
import sys
import pymongo
import pprint

import pdf_extract

class Database:
    def __init__(self):
        try:
            self.mongo_conn = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mongo_conn.server_info()
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print (err)

        self.mongo_database = self.mongo_conn["Security+"]
        self.mongo_cluster = self.mongo_database["Questions"]

        self.pdf_extract_obj = pdf_extract.PdfExtraction()
    
    def add_entry(self):
        # cluster_id = 1
        # post_document = {
        #     "id": cluster_id, 
        #     "Questions": question, 
        #     "Answer": answer}
        # cluster_id = cluster_id + 1

        question = self.pdf_extract_obj.read_questions()
        cluster_id = 1

        post_question_document = {
            "id" : cluster_id,
            "Questions" : question,
        }

        cluster_id = cluster_id + 1
        self.mongo_cluster.insert_one(post_question_document)

    def query_table(self):
        data_result = self.mongo_cluster.find({})

        for data in data_result:
            if self.check_for_duplicate(data) is False:
                print(data)
    
    def query_table_entry(self, item):
        return self.mongo_cluster.find_one(item)

    def check_for_duplicate(self, question):
        query_result = self.query_table_entry(question)
        
        pprint.pprint(query_result)

        return True if query_result is False else False
    
    def update_table_entry(self, item):
        self.mongo_cluster.delete_one(item)

    def __drop_cluster(self):
        self.mongo_cluster.drop()

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
#     sample_question = """
#     1. Which of the following will MOST likely adversely impact the operations of unpatched traditional programmable-logic controllers, running a back-end LAMP server and OT systems with human-management interfaces that are accessible over the Internet via a web interface? (Choose two.)
# A. Cross-site scripting
# B. Data exfiltration
# C. Poor system logging
# D. Weak encryption
# E. SQL injection
# F. Server-side request forgery"""

#     sample_question_answer = "Answers: D and F"

#     question = Questions()
#     question.add_entry(sample_question, sample_question_answer)
#     question.print_table()

##################################
    # mongo_conn = pymongo.MongoClient("mongodb://localhost:27017/")
    # mongo_database = mongo_conn["Security+"]
    # mongo_cluster = mongo_database["Questions"]    

    # mydict = { "name": "John", "address": "Highway 37" }

    # random_insert =  mongo_cluster.insert_one(mydict)

    # print(mongo_conn.server_info())

    database = Database()
    #database.query_table()

    example_document = {'name': 'John'}
    database.query_table()