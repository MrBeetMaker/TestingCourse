import unittest
import pickle
import hashlib

obj = {"asfd":34}
with open('object.pickle', 'wb') as f:
    pickle.dump(obj, f)


# Unpickle the object
with open('object.pickle', 'rb') as f:
    loaded_obj = pickle.load(f)
    f.seek(0)
    print(f.read())

print(hashlib.sha256(obj))
print(hashlib.sha256(loaded_obj))
