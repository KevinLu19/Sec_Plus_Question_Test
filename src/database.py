from unittest import result
import pymongo
import pprint

class Database:
    connection = None   # used to connect to the database once and not per instance.

    def __init__(self):
        if Database.connection is None:
            try:
                self.mongo_conn = pymongo.MongoClient("mongodb://localhost:27017/")
                self.mongo_conn.server_info()

            except pymongo.errors.ServerSelectionTimeoutError as err:
                print (err)

        self.connection = Database.connection
        self.mongo_database = self.mongo_conn["Security+"]
        self.mongo_cluster = self.mongo_database["Questions"]


    def add_entry(self, sec_plus_questions):
        cluster_id = 1

        post_question_document = {
            "id" : cluster_id,
            "Questions" : sec_plus_questions,
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

    def query_question_column(self):
        for query_questions in self.mongo_cluster.find({ "Questions": { "$exists": True } }):
            pprint.pprint(query_questions['Questions'])

    def check_for_duplicate(self, question):
        query_result = self.query_table_entry(question)
        
        pprint.pprint(query_result)

        return True if query_result is False else False
    
    def update_table_entry(self, item):
        self.mongo_cluster.delete_one(item)

    def __drop_cluster(self):
        self.mongo_cluster.drop()

if __name__ == "__main__":
    database = Database()
    database.query_question_column()