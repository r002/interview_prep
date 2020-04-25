import unittest

class Hello():
    def run()->'This is the main runner':
        print("hello there!")


def is_odd(number: int)->bool:
    return True if number % 2 == 1 else False


class Test_Odd(unittest.TestCase):
    dataT = [(123), (455)]
    def test_odd(self):
        for case in self.dataT:
            actual = is_odd(case)
            self.assertTrue(actual)


class Test_Even(unittest.TestCase):
    dataF = [(1234), (4554)]

    def test_even(self):
        for case in self.dataF:
            actual = is_odd(case)
            self.assertFalse(actual)


if __name__ == "__main__":
    # Hello.run()
    unittest.main()
