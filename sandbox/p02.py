# Extract second largest number from a list

import unittest

def is_number(s:str)->bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


class Extractor():
    def __init__(self, l:list):
        self.inputted_list = l
        self.unique_list = None
        self.result = (False, "Error00", "Default Error")

        if self.validate(): self.extract()

        print(f"\nOriginal list: {self.inputted_list}")
        print(self.result)

    def validate(self)->bool:
        str_list = [str(item) for item in self.inputted_list]
        clean_list = [int(item) for item in str_list if is_number(item)]
        unique_list = list(set(clean_list))

        if len(unique_list)<2:
            self.result = (False, "Error01", "Insufficient unique numbers in inputted list.")
            return False

        self.unique_list = unique_list
        return True

    def extract(self):
        self.unique_list.sort()
        largest_number = self.unique_list[-2]
        self.result = (True, largest_number, "Success!")


class Test(unittest.TestCase):
    t00 = [1, 1, 1]
    t01 = [1, 99, 3]
    t02 = [5, 5, 2, 3, "aaa", "", 0, 1.1, -4, True, False]

    def test00(self):
        actual = Extractor(self.t00)
        self.assertEqual(False, actual.result[0])

    def test01(self):
        actual = Extractor(self.t01)
        self.assertEqual(3, actual.result[1])

unittest.main()
