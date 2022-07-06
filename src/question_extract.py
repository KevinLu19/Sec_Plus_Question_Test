import database

class QuestionExtraction:
    def __init__(self, question_file) -> None:
        self.text_file = question_file
        self.database_has_a_relationship = database.Questions()

    def read_question(self):
        answer = []
        question = []

        with open(self.text_file) as txt:
            read_lines = txt.readlines()

            for item in read_lines:
                if "Answer" in item:
                    answer.append(item)
                else:
                    question.append(item)
        print(question)
        print(answer)

        self.add_question_to_database(question, answer)
    
    def add_question_to_database(self, question, answer):
        self.database_has_a_relationship.add_entry(question, answer)

def main():
    text_file = "questions.txt"

    question_class = QuestionExtraction(text_file)
    question_class.read_question()

if __name__ == "__main__":
    main()