# String compression

import unittest

def compress(s:str)->str:
    if len(s)==0:
        return False

    rs = []
    current_letter = s[0]
    counter = 1
    ss = s[1:]

    for letter in ss:
        if current_letter == letter:
            counter += 1
        else:
            rs.append(current_letter)
            if counter != 1: rs.append(counter)
            current_letter = letter
            counter = 1

    # Append last repeated char
    rs.append(current_letter)
    if counter != 1: rs.append(counter)

    rs = "".join([str(_) for _ in rs])

    if len(rs) < len(s):
        return rs
    else:
        return s

class Test(unittest.TestCase):
    '''Test Cases'''
    t00 = [
        ("aabcccaa", "a2bc3a2"),
        ('aabcccccaaa', 'a2bc5a3'),
        ('abcdef', 'abcdef')
    ]

    def test00(self):
        for testcase, result in self.t00:
            actual = compress(testcase)
            self.assertEqual(actual, result)


unittest.main()
