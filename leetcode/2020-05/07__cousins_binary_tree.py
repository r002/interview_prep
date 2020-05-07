import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Assumptions:
# 1. x and y are guaranteed to be in the tree.
# 2. x and y are different nodes.
# 3. There exist 2-100 nodes in the tree.
# 4. Each node has a unique val.

class Solution:
    def __init__(self):
        self.xParent = None
        self.xDepth  = None
        self.yParent = None
        self.yDepth  = None

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # Check edge cases:
        if (x == root.val) or (y == root.val):
            return False

        self.walkTree(root, 0, x, y)
        print()
        print(f"xParent: {self.xParent} | yParent: {self.yParent}")
        print(f"xDepth: {self.xDepth} | yDepth: {self.yDepth}")

        # if self.xParent != None and self.yParent != None:  # x and y are guaranteed to be in the tree so we don't need this check.
        if (self.xDepth == self.yDepth) and (self.xParent != self.yParent):
            return True
        else:
            return False

    def walkTree(self, root:TreeNode, depth:int, x:int, y:int):
        print(f"\n{root.val} -- depth: {depth}")
        left = root.left.val if root.left != None else None
        right = root.right.val if root.right != None else None
        print(f"{left} | {right}")

        # Is left or right the val we seek? If so, remember the parent and depth.
        if x == left or x == right:
            self.xParent = root.val
            self.xDepth = depth

        if y == left or y == right:
            self.yParent = root.val
            self.yDepth = depth

        # May we quit? Or do we keep walking the tree?
        if (self.xParent != None) and (self.yParent != None):
            return
        else:
            # Keep walking the tree
            if root.left != None:
                self.walkTree(root.left, depth+1, x, y)

            if root.right != None:
                self.walkTree(root.right, depth+1, x, y)

#####################################################################################

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
            self.assertEqual(result, expected)

unittest.main()
