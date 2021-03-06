import PyPDF2

class PdfExtraction:
    def __init__(self):
        self.pdf_file_object = open("questions.pdf", "rb")
        self.pdf_reader = PyPDF2.PdfFileReader(self.pdf_file_object)
    
    def read_questions(self):
        for question in range(3, 137):
            page_object = self.pdf_reader.getPage(question)
            extracted_questions = page_object.extractText()

            self.remove_text_from_pdf(extracted_questions)
            # print (extracted_questions)

        self.pdf_file_object.close()


    def remove_text_from_pdf(self, question_bank : str):
        for removal_text in ["Licensed to Christi Sanders", "clynsanders@outlook.com"]:
            if removal_text in question_bank:
                questions = question_bank.replace(removal_text, "")

        print (questions)
        
            

if __name__ == "__main__":
    pdf = PdfExtraction()
    pdf.read_questions()