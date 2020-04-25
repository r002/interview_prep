# From a list, extract the second largest number

import unittest

def is_number(s:str)->bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


class extract_result():
    def __init__(self, input_list:list)->'This is the constructor':
        self.result = (False, "Error00", "Default error message")
        self.input_list = input_list

        if self.validate_input(): self.perform_extraction()

        print()
        print(f"Original list: {input_list}")
        print(self.result)

    def perform_extraction(self)->"Extract second largest number":
        # print("\nperform extraction!")
        # print(self.cleaned_list)
        l = list(self.cleaned_list)
        l.sort()
        # print(l)
        answer = l[-2]
        self.result = (True, answer, "Success! Second largest number.")

    def validate_input(self)->"self.result":
        # Convert all list items into strings
        stringified_list = [str(item) for item in self.input_list]
        # print(stringified_list)

        cleaned_list = [item for item in stringified_list if is_number(item)]
        # print(cleaned_list)

        cleaned_list = [int(item) for item in cleaned_list]
        # print(cleaned_list)

        cleaned_list = set(cleaned_list)
        # print(cleaned_list)

        if len(cleaned_list) < 2:
            self.result = (False, "Error01", "Insufficient unique numbers in inputted list.")
            return False
        else:
            self.cleaned_list = cleaned_list
            return True


class Test(unittest.TestCase):
    t01 = [123, 456, "aaa", "555", "", -1, -1, 1.1]
    t02 = [123, 123, 123]
    t03 = [123, 456]

    def test01(self):
        actual = extract_result(self.t01)
        self.assertEqual(actual.result[1], 456)

    def test02(self):
        actual = extract_result(self.t02)
        self.assertEqual(actual.result[0], False)

    def test03(self):
        actual = extract_result(self.t03)
        self.assertEqual(actual.result[1], 123)

unittest.main()

# p = extract_result([123, 456, "aaa", "555", "", -1, -1, 1.1])
# p = extract_result([123, 123, 123])
# p = extract_result([123, 456])
