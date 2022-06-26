import unittest

class TestQuestionExtract(unittest.TestCase):
    def setUp(self) -> None:
        self.answer_options = ["A", "B", "C", "D"]
        self.sample_question = "1. Which of the following will MOST likely adversely impact the operations of unpatched traditional programmable-logic controllers, running a back-end LAMP server and OT systems with human-management interfaces that are accessible over the Internet via a web interface? (Choose two.)"
    
    def test_question(self):
        simulated_question_answer = "D and F"

        # return self.assertEqual()

def main():
    unittest.main()


if __name__ == "__main__":
    main()