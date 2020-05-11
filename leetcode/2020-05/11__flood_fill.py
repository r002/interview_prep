import unittest

class Solution:
    def __init__(self):
        self.oldColor = None
        self.newColor = None
        self.image = None

    def floodFill(self, image:list, sr:int, sc:int, newColor:int) -> list:
        # Print original
        print("Original:")
        for row in image:
            print(row)
        print("---")

        self.oldColor = image[sr][sc]
        self.newColor = newColor
        self.image = image
        self.rowsNum = len(image)
        self.colsNum = len(image[0])

        # If newColor == oldColor, just return the original image.
        if newColor == image[sr][sc]:
            return image
        else:
            self.fillRecursive(sr, sc)

        print("New:")
        for row in self.image:
            print(row)

        return self.image


    def fillRecursive(self, sr, sc):
        # Change the pixel's color
        self.image[sr][sc] = self.newColor

        # Fill all applicable adjacent pixels
        self.fillAbove(sr, sc)
        self.fillBelow(sr, sc)
        self.fillLeft(sr, sc)
        self.fillRight(sr, sc)


    def fillAbove(self, row, col):
        if row-1 >= 0:
            if self.image[row-1][col] == self.oldColor:
                self.fillRecursive(row-1, col)

    def fillBelow(self, row, col):
        if row+1 < self.rowsNum:
            if self.image[row+1][col] == self.oldColor:
                self.fillRecursive(row+1, col)

    def fillLeft(self, row, col):
        if col-1 >= 0:
            if self.image[row][col-1] == self.oldColor:
                self.fillRecursive(row, col-1)

    def fillRight(self, row, col):
        if col+1 < self.colsNum:
            if self.image[row][col+1] == self.oldColor:
                self.fillRecursive(row, col+1)


class Test(unittest.TestCase):
    cases = [
        ([[1,1,1],
          [1,1,0],
          [1,0,1]], 2, 2, 2,
         [[1,1,1],
          [1,1,0],
          [1,0,2]]),
        ([[1,1,1],
          [1,1,9],
          [1,9,9]], 2, 2, 7,
         [[1,1,1],
          [1,1,7],
          [1,7,7]]),
        ([[1]], 0, 0, 1,
         [[1]]),
        ([[1]], 0, 0, 2,
         [[2]]),
        ([[1,1,1],
          [1,1,0],
          [1,0,1]], 1, 1, 2,
         [[2,2,2],
          [2,2,0],
          [2,0,1]]),
        ([[1,1,1],
          [1,1,0],
          [1,0,1]], 1, 1, 1,
         [[1,1,1],
          [1,1,0],
          [1,0,1]]),
        ([[1,1,1],
          [1,1,0],
          [1,0,1]], 0, 0, 2,
         [[2,2,2],
          [2,2,0],
          [2,0,1]])
    ]

    def test0(self):
        for image, sr, sc, newColor, expected in self.cases:
            s = Solution()
            result = s.floodFill(image, sr, sc, newColor)
            # print(f"{image} | {sr} | {sc} | {newColor}")
            # print(f"{result}")
            # print(f"{expected}")
            self.assertEqual(result, expected)


unittest.main()
