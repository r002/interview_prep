import unittest
from collections import Counter

# Source: https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1:str, s2:str)->bool:
        if len(s2)<len(s1):
            return False

        s1c = Counter(s1)
        s1_len = len(s1)
        s2c = Counter(s2[0:s1_len])
        if s1c==s2c:
            return True

        for i in range(1, len(s2)-s1_len+1):
            # print(f"{i} | old window: {s2c}")
            left_letter = s2[i-1]
            s2c[left_letter] -= 1
            if s2c[left_letter] == 0: del s2c[left_letter]

            next_letter = s2[s1_len-1+i]
            s2c[next_letter]+=1
            # print(f"{i} | new window: {s2c}")
            if s1c==s2c:
                return True

        return False

class Test(unittest.TestCase):
    cases = [
        ("", "", True),
        ("", "abc", True),
        ("abc", "abc", True),
        ("a", "bbbbbbbbba", True),
        ("ac", "bbbbbbbbbca", True),
        ("a", "aaaa", True),
        ("cbaebabacd", "abc", False),
        ("abc", "cbaebabacd", True),
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False)
    ]
    s = Solution()

    def test0(self):
        for s, p, expected in self.cases:
            result = self.s.checkInclusion(s, p)
            print(f"RESULT: {s} | {p} | {result} | {expected}")
            self.assertEqual(result, expected)
            print("---")


unittest.main()
