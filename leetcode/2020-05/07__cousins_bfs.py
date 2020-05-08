from collections import deque
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    xParent = None
    xDepth = None
    yParent = None
    yDepth = None

    def isCousins(self, root:TreeNode, x:int, y:int)->bool:
        dq = deque([(root, 0, -1)])
        while dq:
            node, depth, parentVal = dq.popleft()
            print(f"val: {node.val} | depth: {depth} | parentVal: {parentVal}")

            if node.val == x:
                self.xParent = parentVal
                self.xDepth = depth
            elif node.val == y:
                self.yParent = parentVal
                self.yDepth = depth

            # Do we quit or keep walking the tree?
            if self.xParent != None and self.yParent !=None:
                break

            # Keep walking the tree
            if node.left:
                dq.append((node.left, depth+1, node.val))
            if node.right:
                dq.append((node.right, depth+1, node.val))

        # Check if x and y are cousins
        print("---")
        print(f"x: {x} | xParent: {self.xParent} | xDepth: {self.xDepth}")
        print(f"y: {y} | yParent: {self.yParent} | yDepth: {self.yDepth}")

        if self.xDepth == self.yDepth and self.xParent != self.yParent:
            return True

        return False


########################################################################

n6 = TreeNode(6, None, None)
n5 = TreeNode(5, n6, None)
n4 = TreeNode(4, None, None)
n3 = TreeNode(3, None, n5)
n2 = TreeNode(2, n4, None)
n1 = TreeNode(1, n2, n3)

class Test(unittest.TestCase):
    cases = [
        (1, 2, False),
        (3, 2, False),
        (2, 3, False),
        (4, 3, False),
        (4, 5, True),
        (5, 4, True)
    ]

    def test(self):
        for x, y, expected in self.cases:
            s = Solution()
            result = s.isCousins(n1, x, y)
            print(f"{x} | {y} | {result} | {expected}")
            print()
            self.assertEqual(result, expected)

unittest.main()
