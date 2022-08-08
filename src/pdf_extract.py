import PyPDF2
import database


class PdfExtraction:
    MONGO_DATABASE = database.Database()

    def __init__(self):
        self.pdf_file_object = open("questions.pdf", "rb")
        self.pdf_reader = PyPDF2.PdfFileReader(self.pdf_file_object)

        self.mongo_database = PdfExtraction.MONGO_DATABASE

    def read_questions(self):
        for question in range(3, 137):
            page_object = self.pdf_reader.getPage(question)
            extracted_questions = page_object.extractText()

            self.remove_text_from_pdf(extracted_questions)
            # print (extracted_questions)

        page_object = self.pdf_reader.numPages

    def remove_text_from_pdf(self, question_bank : str):
        for removal_text in ["Licensed to Christi Sanders", "clynsanders@outlook.com"]:
            if removal_text in question_bank:
                questions = question_bank.replace(removal_text, "")
                print (questions)
                
                self.mongo_database.add_entry(questions)
                self.copy_to_txt_file(questions)
        
        return questions

    def copy_to_txt_file(self, questions : str):
        with open("questions.txt", "w", encoding="utf-8") as file:
            file.write(questions)

    def __exit__(self):
        self.pdf_file_object.close()

if __name__ == "__main__":
    pdf = PdfExtraction()
    pdf.read_questions()
    