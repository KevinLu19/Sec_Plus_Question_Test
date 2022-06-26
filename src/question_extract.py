from distutils.text_file import TextFile
import re

class QuestionExtraction:
    def __init__(self, question_file) -> None:
        self.text_file = question_file

    def read_question(self):
        answer = []
        question = []

        with open(self.text_file) as txt:
            read_lines = txt.readlines()

            if "Answer" in read_lines:
                txt.split()

def main():
    text_file = "questions.txt"

    question_class = QuestionExtraction(text_file)
    question_class.read_question()

if __name__ == "__main__":
    main()