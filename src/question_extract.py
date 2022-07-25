import database

from pathlib import Path

class ImportingQuestion:
    def __init__(self):
        self.change_directory = Path(r"../src/questions.txt") 

class QuestionExtraction:
    def __init__(self) -> None:
        self._importing_class = ImportingQuestion()
        self.extracted_question = self._importing_class.change_directory
        self.database_has_a_relationship = database.Questions()

    def read_question(self):
        answer_list = []
        question_list = []

        with open(self.extracted_question) as txt:
            for question in txt:
                if "Answer" in question:
                    answer = question.splitlines()
                    answer_list.append(answer)
                else:
                    question_list.append(question)

        # print (question_list)
        # print (answer_list)          

        self.add_question_to_database(question_list, answer_list)
    
    def add_question_to_database(self, question_list, answer_list):
        for  question in question_list:
            print (question)
        
        for answer in answer_list:
            print ( answer)

        # self.database_has_a_relationship.add_entry(question, answer)

def main():
    # text_file = "questions.txt"

    # question_class = QuestionExtraction(text_file)
    # question_class.read_question()
    question = QuestionExtraction()
    question.read_question()

if __name__ == "__main__":
    main()