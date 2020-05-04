import unittest

class Solution:
    def findComplement(self, num: int) -> int:
        # Convert number to its binary literal representation
        binlit = format(num, 'b')
        binlit = binlit[::-1]  # Reverse the string

        # Invert the binary literal
        invlit = [int(not int(_)) for _ in binlit]
        invlit = "".join(str(_) for _ in invlit)
        invlit.strip('0')  # Remove all trailing zeroes

        # Convert binary literal to number
        rs = 0
        for power, include in enumerate(invlit):
            if int(include): rs += 2**power

        return rs


class Test(unittest.TestCase):
    t0 = [
        (5, 2),  # 101 -> 010
        (0, 1),  # 0 -> 1
        (1, 0),  # 1 -> 0
        (3, 0),  # 11 -> 00
        (7, 0),  # 111 -> 000
        (8, 7),  # 0001 -> 1110
        (10, 5)  # 0101 -> 1010
    ]
    s = Solution()

    def test0(self):
        for testcase, expected in self.t0:
            result = self.s.findComplement(testcase)
            print(f"{testcase} | {result} | {expected}")
            self.assertEqual(result, expected)

unittest.main()
