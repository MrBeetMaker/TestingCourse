import pickle
import hashlib
import os
import platform
import sys

def hash_pickle(data):
    pickle_data = pickle.dumps(data)
    return hashlib.sha256(pickle_data).hexdigest()

def run_tests(test_cases):
    results = {}
    for i, case in enumerate(test_cases):
        hash_value = hash_pickle(case)
        results[f"case_{i}"] = hash_value
    return results

class SimpleClass:
    def __init__(self, value):
        self.value = value

class RecursiveClass:
    def __init__(self):
        self.self = self


if __name__ == "__main__":
    test_cases = [
        42,
        3.14159,
        "Hello, World!",
        [1, 2, 3, 4, 5],
        {"key1": "value1", "key2": "value2"},
        [],
        {},
        SimpleClass(10),
        RecursiveClass(),
    ]
    test_cases[-2].append(test_cases[-2])  # recursive list
    test_cases[-1]["self"] = test_cases[-1]  # recursive dict

    results = run_tests(test_cases)
    os_name = platform.system()
    python_version = sys.version.split()[0]
    
    with open(f"results_{os_name}_{python_version}.txt", "w") as f:
        for case, hash_value in results.items():
            f.write(f"{case}: {hash_value}\n")
