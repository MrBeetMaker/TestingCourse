import unittest
import pickle
import hashlib

pickle_dump_file = ".\\dump_file.bin"

class SimpleClass:
    def __init__(self, value):
        self.value = value

    def add(a, b):
        return a + b + b + a + b + a

class RecursiveClass:
    def __init__(self):
        self.self = self

def pickle_and_hash(data):
    pickled_data = pickle.dumps(data, protocol=4)
    return hashlib.sha256(pickled_data, usedforsecurity= False).hexdigest()

def pickle_unpickle_repickle_and_hash(data):
    pickled_data = pickle.dumps(data, protocol=4)
    unpickled_data = pickle.loads(pickled_data)
    re_pickled_data = pickle.dumps(unpickled_data, protocol=4)
    return hashlib.sha256(re_pickled_data, usedforsecurity= False).hexdigest()

class TestPickle(unittest.TestCase):

    def assertPickleHashIdentical(self, data):
        pickled_data = pickle_and_hash(data)
        repickled_data = pickle_unpickle_repickle_and_hash(data)
        self.assertEqual(pickled_data, repickled_data)

    def test_int(self):
        self.assertPickleHashIdentical(42)

    def test_float(self):
        self.assertPickleHashIdentical(3.1415926535)

    def test_string(self):
        self.assertPickleHashIdentical("Hello, World!")

    def test_list(self):
        self.assertPickleHashIdentical([1, 2, 3, 4, 5])

    def test_dict(self):
        self.assertPickleHashIdentical({"key1": "value1", "key2": "value2"})

    def test_empty_list(self):
        self.assertPickleHashIdentical([])

    def test_empty_dict(self):
        self.assertPickleHashIdentical({})

    def test_simple_class(self):
        self.assertPickleHashIdentical(SimpleClass(10))

if __name__ == '__main__':
    unittest.main()
