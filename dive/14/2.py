class BNFError(Exception):
    def __init__(self):
        super().__init__("!")
    
class Lib:
    def __init__(self):
        self.books = set()

    def add(self, book):
        self.books.add(book)

    def remove(self, book):
        if book not in self.books: raise BNFError()
    
        self.books.remove(book)

    def list(self):
        return list(self.books)

import unittest

class TestLib(unittest.TestCase):
    def setUp(self):
        self.lib = Lib()
        return super().setUp()

    def test_add(self):
        self.lib.add("x")
        self.assertIn("x", self.lib.list())

    def test_rm(self):
        with self.assertRaises(BNFError):
            self.lib.remove("y")

if __name__ == "__main__":
    unittest.main()