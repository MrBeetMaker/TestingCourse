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


def hash_object(data):
    if isinstance(data, str):
        data = data.encode()
    elif not isinstance(data, bytes):
        data = pickle.dumps(data)
    return hashlib.sha256(data).hexdigest()

def hash_after_pickle(data):
    unpickled_data = pickle.loads(pickle.dumps(data))

    return hashlib.sha256(unpickled_data).hexdigest()


class TestPickle(unittest.TestCase):
    def test_int(self):
        self.assertEqual(hash_after_pickle(42), hash_object(42))

    def test_float(self):
        self.assertEqual(hash_after_pickle(3.14159), hash_object(3.14159))

    def test_string(self):
        self.assertEqual(hash_after_pickle("Hello, World!"), hash_object("Hello, World!"))

    def test_list(self):
        self.assertEqual(hash_after_pickle([1, 2, 3, 4, 5]), hash_object([1, 2, 3, 4, 5]))

    def test_dict(self):
        self.assertEqual(hash_after_pickle({"key1": "value1", "key2": "value2"}), hash_object({"key1": "value1", "key2": "value2"}))

    def test_empty_list(self):
        self.assertEqual(hash_after_pickle([]), hash_object([]))

    def test_empty_dict(self):
        self.assertEqual(hash_after_pickle({}), hash_object({}))

    def test_simple_class(self):
        self.assertEqual(hash_after_pickle(SimpleClass(10)), hash_object(SimpleClass(10)))

    def test_recursive_class(self):
        with self.assertRaises(pickle.PicklingError):
            hash_after_pickle(RecursiveClass())


if __name__ == '__main__':
    unittest.main()
