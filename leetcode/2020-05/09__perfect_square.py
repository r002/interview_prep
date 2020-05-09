import unittest

# May 9, 2020: 'Valid Perfect Square'
# https://leetcode.com/problems/valid-perfect-square
#
# Assumptions:
# 1. num is a positive integer (eg. not zero)

class Solution:
    def __init__(self):
        self.originalNum = None
        self.upperBound = None
        self.lowerBound = None
        self.root = None

    def isPerfectSquare(self, num:int) -> bool:
        # Manually handle edge cases:
        if num==1: return True
        if num==2: return False

        # Run my algo; works for all num > 2:
        self.originalNum = num
        self.upperBound = num

        rs = self.solve(num)
        print(f"Original: {self.originalNum}")
        print(f"Upper: {self.upperBound}")
        print(f"Lower: {self.lowerBound}")
        print(f"Root: {self.root}")
        return rs

    def solve(self, num:int) -> bool:
        half = num//2
        print(f"{num} -> {half}")

        if half**2 == self.originalNum:
            self.root = half
            return True
        elif half**2 > self.originalNum:
            self.upperBound = half
            return self.solve(half)
        elif half**2 < self.originalNum:
            self.lowerBound = half
            # Now we have the upper and lower bounds,
            # search to see if the root exists.
            for i in range(self.lowerBound+1, self.upperBound):
                if i**2 == self.originalNum:
                    self.root = i
                    return True
                elif i**2 > self.originalNum:
                    return False

            # If the root isn't between the upper and lower bounds, return False.
            # At this point, root can't possibly exist.
            return False


class Test(unittest.TestCase):
    cases = [
        (1, True),
        (2, False),
        (3, False),
        (4, True),
        (5, False),
        (6, False),
        (7, False),
        (8, False),
        (9, True),
        (899, False),
        (900, True),
        (14, False),
        (16, True)
    ]

    def test00(self):
        for test, expected in self.cases:
            s = Solution()
            result = s.isPerfectSquare(test)
            print(f"{test} | {result} | {expected}")
            print("---")
            self.assertEqual(result, expected)

unittest.main()
