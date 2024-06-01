import pickle
import platform
import sys
import csv
import hashlib

class TestPickle():

    def __init__(self) -> None:
        os_info = f"{platform.system()}_{platform.release()}_{platform.version()}"
        python_version = sys.version.split()[0]
        self.file_name = f"results_{os_info}_{python_version}.csv"

    @property
    def test_cases(self):

        test_cases = [
            42,
            3.14159,
            "Hello, World!",
            [1, 2, 3, 4, 5],
            {"key1": "value1", "key2": "value2"},
            [],
            {},
            (1, 1),
            ('a', 'b')
            ]
        return test_cases

    def run_tests(self):
        for i, test_case in enumerate(self.test_cases):
            self.process(test_case, i)

        self.validate_test_results()

    @staticmethod
    def pickle_and_hash(data) -> tuple:
        """Returns the hash and the pickled data."""
        pickled_data = pickle.dumps(data, protocol=0)
        return hashlib.sha256(pickled_data, usedforsecurity= False).hexdigest(), pickled_data

    @staticmethod
    def pickle_unpickle_repickle_and_hash(data) -> tuple:
        """Pickles the data, unpickles it, pickles it again and hashes it.
        
        Returns the hash, the pickled data, and the repickled data."""
        pickled_data = pickle.dumps(data, protocol=0)
        unpickled_data = pickle.loads(pickled_data)
        re_pickled_data = pickle.dumps(unpickled_data, protocol=0)
        return hashlib.sha256(re_pickled_data, usedforsecurity= False).hexdigest(), pickled_data, re_pickled_data

    def process(self, data, test_nr):
        """Collects and saves two separate dumps of the pickled data, the repickled data, 
        the hash of the first pickled object and the hash of the repickled object."""

        phash, pickled_data_1 = self.pickle_and_hash(data)

        re_phash, pickled_data_2, repickled_data = self.pickle_unpickle_repickle_and_hash(data)

        # Save the data
        with open(self.file_name, "a") as f:
            f.write(f"{test_nr};{pickled_data_1};{pickled_data_2};{repickled_data};{phash};{re_phash}\n")

    def validate_test_results(self):

        with open(self.file_name) as file:
            results = csv.reader(file, delimiter= ";")

            for res in results:

                test_nr, pickled_data_1, pickled_data_2, repickled_data, phash, re_phash = res

                test_results = f"Test case #{test_nr}:\n"

                if not pickled_data_1 == pickled_data_2:
                    test_results += "\t- Different pickles of same data.\n"
                if not pickled_data_1 == repickled_data:
                    test_results += "\t- Repickled data different than first pickle.\n"
                if not pickled_data_2 == repickled_data:
                    test_results += "\t- Repickled data different than second pickle.\n"
                if not phash == re_phash:
                    test_results += "\t- Hash different for repickled data.\n"

                if len(test_results) < 20:
                    test_results += "\t- Passed all checks."

                print(test_results)

if __name__ == "__main__":
    TestPickle().run_tests()

