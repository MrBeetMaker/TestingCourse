import pickle

pickle_dump_file = ".\\dump_file.bin"

class TestClass():
    def __init__(self) -> None:
        pass

    def func():
        return 1

before = TestClass()

with open(pickle_dump_file, 'wb') as f:
    pickle.dump(before, f)

with open(pickle_dump_file, 'rb') as f:
    after = pickle.load(f)

