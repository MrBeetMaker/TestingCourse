import unittest
import pickle

class TestPickle(unittest.TestCase):

    def test(self):

        class Adder():

            def __init__(self) -> None:
                self._val = 10

            def add(a, b):
                1 + 2
                a + b
                2 + 1
                b + a
                return a + b + b + a + b + a


        with open(pickle_dump_file, 'wb') as f:
            pickle.dump(before, f)

        with open(pickle_dump_file, 'rb') as f:
            after = pickle.load(f)


        self.assertEqual()

if __name__ == '__main__':
    unittest.main()
