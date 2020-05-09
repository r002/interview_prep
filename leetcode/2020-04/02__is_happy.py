import unittest

class Solution:
    def __init__(self):
        self.s = set()

    def isHappy(self, n: int) -> bool:
        self.s.add(n)
        sum = 0
        for digit in list(str(n)):
            sum += int(digit)**2

        print(f"{n} -> {sum}")

        if sum == 1:
            return True
        elif sum in self.s:
            return False
        else:
            return self.isHappy(sum)


class Test(unittest.TestCase):
    cases = [
        (2, False),
        (1, True),
        (0, False),
        (19, True)
    ]

    def test(self):
        for n, expected in self.cases:
            s = Solution()
            print(s.s)  # Just visually checking that the set is empty
            result = s.isHappy(n)
            print(f"{n} | {result} | {expected}")
            print("---")
            self.assertEqual(result, expected)

unittest.main()
