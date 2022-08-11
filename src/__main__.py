from .database import Database


def main():
    mongo_database = Database()
    mongo_database.query_question_column()


if __name__ == "__main__":
    main()