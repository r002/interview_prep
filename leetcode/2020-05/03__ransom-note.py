import unittest

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for letter in ransomNote:
            if letter in magazine:
                magazine.remove(letter)
            else:
                return False
        return True


class Test(unittest.TestCase):
    t0 = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("", "", True),
        ("a", "", False),
        ("", "a", True),
    ]

    s = Solution()

    def test0(self):
        for testcase in self.t0:
            ransomNote, magazine, expected = testcase[0], testcase[1], testcase[2]
            actual = self.s.canConstruct(ransomNote, magazine)
            self.assertEqual(actual, expected)


unittest.main()
