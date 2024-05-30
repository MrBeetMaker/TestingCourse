import unittest
import pickle
import hashlib


class SimpleClass:
    def __init__(self, value):
        self.value = value

    def add(a, b):
        return a + b + b + a + b + a


obj = SimpleClass(3)
obj1 = SimpleClass(3)

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
