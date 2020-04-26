# Check to see if a given string has any permutations that is a palindrome.

import unittest
import collections

def convert_to_ascii(s:str)->list:
    return [ord(_) for _ in s]


def is_odd(num:int)->bool:
    return (num % 2) == 1

def pal_perm(phrase):
    # Strip all spaces and convert to lowercase
    phrase = phrase.lower()
    phrase = "".join(phrase.split())
    # print(phrase)

    c = collections.Counter(phrase)

    odd_counter = 0
    for item in c.items():
        if is_odd(item[1]):
            odd_counter += 1

    if(odd_counter == 0 or odd_counter == 1):
        return True
    else:
        return False


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test(self):
        for test, result in self.data:
            print(f"{test} : {result}")
            self.assertEqual(pal_perm(test), result)

unittest.main()
