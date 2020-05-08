# Assumptions:
# 1. There are guaranteed to be at least two points in the given coordinates list.
# 2. There are no duplicate coordinates.

import unittest

class Solution:
    def checkStraightLine(self, coordinates:list) -> bool:
        if len(coordinates) == 2:  # Two points always make a straight line.
            return True

        # Sort coordinates in ascending order by x
        coordinates = sorted(coordinates, key=lambda item: item[0])  # Same as coordinates.sort()

        # Get the slope
        y1 = coordinates[1][1]
        y0 = coordinates[0][1]
        x1 = coordinates[1][0]
        x0 = coordinates[0][0]

        if x0==x1:
            return self.checkVerticalLine(coordinates)

        slope = (y1-y0)/(x1-x0)

        # Check if remaining coordinates follow the slope
        for x, y in coordinates[2:]:
            if x0==x:
                return False  # If line wasn't vertical earlier, it's impossible to be vertical now.
            if (y-y0)/(x-x0) != slope:
                return False
        return True

    def checkVerticalLine(self, coordinates:list) -> bool:
        x0 = coordinates[0][0]
        for x, y in coordinates[1:]:
            if x != x0: return False
        return True


# [[x1, y1], [x2, y2]]
class Test(unittest.TestCase):
    cases = [
        ([(3,2), (6,4), (12,8)], True),         # Check if slope can be repeating decimal, 2/3~.67
        ([(2,3), (4,6), (8,12)], True),
        ([(0,0), (0,1), (99,4)], False),
        ([(0,0), (1,1), (0,4)], False),
        ([(0,0), (1,1), (4,0)], False),
        ([(0,0), (0,1), (0,2)], True),           # Vertical line
        ([(0,0), (1,0), (2,0)], True),           # Horizontal line
        ([(0,0), (-1,-1), (1,1), (2,2)], True),  # Out of order
        ([(-1,-1), (0,0), (1,1), (2,2)], True),
        (([1,2],[2,3],[3,4],[4,5],[5,6],[6,7]), True),
        (([1,1],[2,2],[3,4],[4,5],[5,6],[7,7]), False)
    ]
    s = Solution()

    def test0(self):
        for coordinates, expected in self.cases:
            result = self.s.checkStraightLine(coordinates)
            print(f"{coordinates} | {result} | {expected}")
            self.assertEqual(result, expected)


unittest.main()
