import enum
import unittest
import os
from pathlib import Path

class TestImportingQuestions(unittest.TestCase):
    def setUp(self) -> None:
        self.change_directory = Path(r"../src/questions.txt")

        return self.change_directory

class TestQuestionExtract(unittest.TestCase):
    def setUp(self) -> None:
        self._test_questions_class = TestImportingQuestions()
        self.extracted_questions = self._test_questions_class.setUp()
 
        self.answer_options = ["A", "B", "C", "D"]
        self.sample_question = "1. Which of the following will MOST likely adversely impact the operations of unpatched traditional programmable-logic controllers, running a back-end LAMP server and OT systems with human-management interfaces that are accessible over the Internet via a web interface? (Choose two.)"
        

    def test_read_question(self):
        question_list = []
        question_answer_list = []

        with open(self.extracted_questions, "r") as file:
            for question in file:
                
                if "Answer" in question:
                    answer = question.splitlines()
                    question_answer_list.append(answer)
                else:
                    question_list.append(question)

                
        # print (question_list)
        print (question_answer_list)

    
        # for item in question_list:
        #     print (item)

        # for ans in question_answer_list:
        #     print(ans)
    


    def test_question_answers(self):
        pass

def main():
    unittest.main()


if __name__ == "__main__":
    main()