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
        self.protocol = 5
        print(f"\nOutput file: {self.file_name}.\n\nNote: Content will be appended.\n")

        self.requirements = {
            1: "Pickling and unpickling integers within and at the edges of the signed 64-bit range.",
            2: "Pickling and unpickling integers within and at the edges of the unsigned 64-bit range.",
            3: "Pickling and unpickling floats with less than 16 decimals.",
            4: "Pickling and unpickling floats with 16 or more decimals.",
            5: "Pickling and unpickling strings with 128 characters or less.",
            6: "",
            7: "Pickling and unpickling lists of floats, integers, and strings with 64 elements or less should return equivalent output.",
            8: "Pickling and unpickling tuples and sets should maintain the order of elements.",
            9: "Time needed to pickle integers and floats within the unsigned 64-bit range, as well as equal-sized strings should never differ by more than 10 milliseconds."
        }

        self._test_case_map = [
            (1337,                      1),
            (2 ** 63 - 1,               1),
            (-(2 ** 63 - 1),            1),

            (2**63 + 100,               2),
            (2**64 - 1,                 2),
            (2**64,                     2),

            (10.0,                      3),
            (0.000280000000015,         3),

            (0.1234567890123456,                            4),
            (0.1234567890123456789,                         4),
            (987654321.123456789012345678901234,            4),

            ("No one inspects the spammish repetition",     5),
            ("e" * 128,                                     5),
            ("",                                            5),

            ([],                        7),
            ([0.324],                   7),
            ([234],                     7),
            (["ddsf"],                  7),
            ([0.324,234,"3dsf"],        7),
            ([i for i in range(64)],    7),
            ([i for i in range(65)],    7),
            (("1", "2", "3", "4", "5", "6"),        8),
            ((),                                    8),
            ]

    def pickle_and_hash(self, data) -> tuple:
        """Returns the hash and the pickled data."""
        pickled_data = pickle.dumps(data, protocol=self.protocol)
        return hashlib.sha256(pickled_data, usedforsecurity= False).hexdigest(), pickled_data

    def pickle_unpickle_repickle_and_hash(self, data) -> tuple:
        """Pickles the data, unpickles it, pickles it again and hashes it.
        
        Returns the hash, the pickled data, the unpickled object, and the repickled data."""
        pickled_data = pickle.dumps(data, protocol=self.protocol)
        unpickled_data = pickle.loads(pickled_data)
        re_pickled_data = pickle.dumps(unpickled_data, protocol=self.protocol)
        return hashlib.sha256(re_pickled_data, usedforsecurity= False).hexdigest(), pickled_data, unpickled_data, re_pickled_data

    def pickle_and_unpickle(self, data):
        """Returns data after it has been pickled and unpickled."""
        pickled_data = pickle.dumps(data, protocol=self.protocol)
        unpickled_data = pickle.load(pickled_data)

        return unpickled_data

    @property
    def test_cases(self):

        test_cases = [pair[0] for pair in self._test_case_map]

        return test_cases

    def run_tests(self):
        unpickled_objects = list()
        for i, test_case in enumerate(self.test_cases):
            obj = self.process(test_case, i)
            unpickled_objects.append(obj)
        self.validate_unpickled_data(unpickled_objects)

        self.validate_test_results()

        self.test_for_mismatches()

    def validate_unpickled_data(self, unpickled_data):
        """Makes sure the unpickled data is unchanged."""

        nr_of_changed_objects = 0
        for test_nr, (original, unpickled) in enumerate(zip(self.test_cases, unpickled_data)):

            if unpickled != original:
                print(f"Test case #{test_nr} was changed after being pickled:\n\t{original} != {unpickled}")
                nr_of_changed_objects += 1

        if nr_of_changed_objects:
            print(f"Pickling changed {nr_of_changed_objects} out of {len(unpickled_data)} objects.\n")
        else:
            print(f"Pickling did not change any of the {len(unpickled_data)} objects.\n")

    def test_for_mismatches(self, iterations = 10000):
        """Pickles the same data many times to see if the result is always the same."""
        errors = []
        print(f"Pickling each test case {iterations} times to find mismatches:")
        for test_nr, test_case in enumerate(self.test_cases):
            first_pickled_data = pickle.dumps(test_case, protocol=self.protocol)
            errors.append([first_pickled_data])
            for _ in range(iterations):
                newly_pickled_data = pickle.dumps(test_case, protocol=self.protocol)

                if newly_pickled_data != first_pickled_data:
                    errors[test_nr].append(newly_pickled_data)

        for test_nr, mismatch in enumerate(errors):
            if len(mismatch) > 1:
                m_string = ""
                for m in mismatch:
                    m_string += f"\n\t\t{m}"
                print(f"\tTest case #{test_nr}:{m_string}")
            else:
                print(f"\tTest case #{test_nr}: - no mismatch")

    def process(self, data, test_nr):
        """Collects and saves two separate dumps of the pickled data, the repickled data, 
        the hash of the first pickled object and the hash of the repickled object."""

        phash, pickled_data_1 = self.pickle_and_hash(data)

        re_phash, pickled_data_2, unpickled_data, repickled_data = self.pickle_unpickle_repickle_and_hash(data)

        # Save the data
        with open(self.file_name, "a") as f:
            f.write(f"{test_nr};{pickled_data_1};{pickled_data_2};{repickled_data};{phash};{re_phash}\n")

        return unpickled_data

    def validate_test_results(self):

        with open(self.file_name) as file:
            results = csv.reader(file, delimiter= ";")

            results_msg = ""
            for res in results:

                test_nr, pickled_data_1, pickled_data_2, repickled_data, phash, re_phash = res

                errors = 0
                error_msg = ""
                if not pickled_data_1 == pickled_data_2:
                    error_msg += "\t- Different pickles for same data.\n"
                    errors += 1
                if not pickled_data_1 == repickled_data:
                    error_msg += "\t- Repickled data different than first pickle.\n"
                    errors += 1
                if not pickled_data_2 == repickled_data:
                    error_msg += "\t- Repickled data different than second pickle.\n"
                    errors += 1
                if not phash == re_phash:
                    error_msg += "\t- Hash different for repickled data.\n"
                    errors += 1

                results_msg += f"Test case #{test_nr}:\n\t- Errors: {errors}\n{error_msg}"

            print(results_msg)

if __name__ == "__main__":
    TestPickle().run_tests()
