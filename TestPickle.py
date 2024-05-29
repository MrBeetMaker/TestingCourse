import unittest
import pickle

pickle_dump_file = ".\\dump_file.bin"

class Adder():

    def __init__(self) -> None:
        self._val = 10

    def add(a, b):
        1 + 2
        a + b
        2 + 1
        b + a
        return a + b + b + a + b + a

class TestPickle(unittest.TestCase):

    def test(self):
        before = Adder()
        with open(pickle_dump_file, 'wb') as f:
            pickle.dump(before, f)

        with open(pickle_dump_file, 'rb') as f:
            after = pickle.load(f)

        self.assertEqual(hash(before), hash(after))

if __name__ == '__main__':
    unittest.main()
