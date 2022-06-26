import sqlite3
import unittest

class TestSQL(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = sqlite3.connect(":memory:")
        cur = self.conn.cursor()
        


def main():
    unittest.main()

if __name__ == "__main__":
    main()