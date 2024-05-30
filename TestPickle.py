import unittest
import stolen_pickle as pickle
import hashlib
import platform
import sys

class ParentClass():
    def __init__(self) -> None:
        self.yahoo = "yippie"

class ChildClass(ParentClass):
    def __init__(self) -> None:
        super().__init__()

class SimpleClass:
    def __init__(self, value):
        self.value = value

    def add(a, b):
        return a + b

class RecursiveClass:
    def __init__(self):
        self.self = self

class TestPickle(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        os_name = platform.system()
        python_version = sys.version.split()[0]
        self.file_name = f"results_{os_name}_{python_version}.csv"

    @staticmethod
    def pickle_and_hash(data):
        """Returns the hash of the pickled data."""
        pickled_data = pickle.dumps(data, protocol=4)
        return hashlib.sha256(pickled_data, usedforsecurity= False).hexdigest()

    @staticmethod
    def pickle_unpickle_repickle_and_hash(data):
        """Pickles the data, unpickles it, pickles it again and hashes it."""
        pickled_data = pickle.dumps(data, protocol=4)
        unpickled_data = pickle.loads(pickled_data)
        re_pickled_data = pickle.dumps(unpickled_data, protocol=4)
        return hashlib.sha256(re_pickled_data, usedforsecurity= False).hexdigest()

    @staticmethod
    def pickle_and_unpickle(data):
        """Returns data after it has been pickled and unpickled."""
        pickled_data = pickle.dumps(data, protocol=4)
        unpickled_data = pickle.loads(pickled_data)
        return unpickled_data

    def assertUnchanged(self, data):
        """Asserts that the data is the same before and after being unpickled."""
        unpickled_data = self.pickle_and_unpickle(data)
        self.assertEquals(data, unpickled_data)

    def assertPickleHashIdentical(self, data):
        """Asserts that the hashes of the data is the same after being pickled once, unpickled and then pickled again.
        Appends the results to the results file."""
        pickled_data = self.pickle_and_hash(data)
        repickled_data = self.pickle_unpickle_repickle_and_hash(data)

        # Save pickled data
        with open(self.file_name, "a") as f:
            f.write(f"{pickled_data},{repickled_data}\n")

        self.assertEqual(pickled_data, repickled_data)

    def test_type_unchanged(self):
        unpickled_obj = self.pickle_and_unpickle(ChildClass())
        self.assertIsInstance(unpickled_obj, ChildClass)

    def test_inheiritance_unchanged(self):
        unpickled_obj = self.pickle_and_unpickle(ChildClass())
        self.assertIsInstance(unpickled_obj, ParentClass)

    def test_int(self):
        self.assertPickleHashIdentical(42)

    def test_function(self):
        self.assertPickleHashIdentical(pow)

    def test_exception(self):
        self.assertPickleHashIdentical(IndexError)

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

    def test_recursive_class(self):
        self.assertPickleHashIdentical(RecursiveClass())

    def test_int_unchanged(self):
        self.assertUnchanged(42)

    def test_function_unchanged(self):
        self.assertUnchanged(pow)

    def test_exception_unchanged(self):
        self.assertPickleHashIdentical(IndexError)

    def test_float_unchanged(self):
        self.assertUnchanged(3.1415926535)

    def test_string_unchanged(self):
        self.assertUnchanged("Hello, World!")

    def test_list_unchanged(self):
        self.assertUnchanged([1, 2, 3, 4, 5])

    def test_dict_unchanged(self):
        self.assertUnchanged({"key1": "value1", "key2": "value2"})

    def test_empty_list_unchanged(self):
        self.assertUnchanged([])

    def test_empty_dict_unchanged(self):
        self.assertUnchanged({})

    # def test_simple_class_unchanged(self):
    #     self.assertUnchanged(SimpleClass(10))

    # def test_recursive_class_unchanged(self):
    #     self.assertUnchanged(RecursiveClass())

if __name__ == '__main__':
    unittest.main()
