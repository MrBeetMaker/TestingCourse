import unittest
import pickle
import hashlib


class SimpleClass:
    def __init__(self, value):
        self.value = 1+value

    def add(self, a, b):
        return a + b + b + a + b + a


class SimpleClass1:
    def __init__(self, value):
        self.value = value + 1

    def add(self, a, b):
        return a + b + b + a + b

    def sub(self):
        pass


obj = SimpleClass(3)
obj1 = SimpleClass1


def test1():

    print(hash(obj))
    print(hash(obj1))
    with open('object.pickle', 'wb') as f:
        pickle.dump(obj, f)

    # Unpickle the object
    sha256_hash = hashlib.sha256()

    with open('object.pickle', 'rb') as f:
        loaded_obj = pickle.load(f)
        for chunk in iter(lambda: f.read(1), b''):
            sha256_hash.update(chunk)

    print(sha256_hash.hexdigest())

    print(hash(loaded_obj))

    print("\n\n")

    print(hash(obj))
    with open('object.pickle', 'wb') as f:
        pickle.dump(obj, f)

    # Unpickle the object
    sha256_hash = hashlib.sha256()
    with open('object.pickle', 'rb') as f:
        loaded_obj = pickle.load(f)
        for chunk in iter(lambda: f.read(64), b''):
            sha256_hash.update(chunk)

    print(sha256_hash.hexdigest())

    print(hash(loaded_obj))

    with open('object1.pickle', 'wb') as f:
        pickle.dump(loaded_obj, f)

    # Unpickle the object
    sha256_hash = hashlib.sha256()

    with open('object1.pickle', 'rb') as f:
        loaded_obj = pickle.load(f)
        for chunk in iter(lambda: f.read(1), b''):
            sha256_hash.update(chunk)

    print(sha256_hash.hexdigest())

    print(hash(loaded_obj))


def test2():
    pickled_data = pickle.dumps(obj, protocol=4)
    print(hashlib.sha256(pickled_data, usedforsecurity=False).hexdigest())
    unpickled_data = pickle.loads(pickled_data)
    pickled_data = pickle.dumps(obj1, protocol=4)
    print(hashlib.sha256(pickled_data, usedforsecurity=False).hexdigest())


test2()
