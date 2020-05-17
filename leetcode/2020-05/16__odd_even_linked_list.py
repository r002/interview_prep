import unittest

# Source: https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head:ListNode) -> ListNode:
        # If head is None, return it. Leetcode caused an error on Test #5:
        # Line 9: AttributeError: 'NoneType' object has no attribute 'next'
        # [] is being passed in?  Doesn't make sense. 5/16/20
        if head == None:
            return head

        # If list is only one node long, return the head
        if head.next == None:
            return head

        oddListHead = head
        # print(f"oddListHead current position: {oddListHead.val}")
        oddListRoot = oddListHead
        evenListHead = head.next
        evenListRoot = evenListHead
        # print(f"evenListHead current position: {evenListHead.val}")

        currentNode = evenListHead.next
        i = 3
        while currentNode != None:  # On the first iteration, currentNode is node #3
            if i % 2 == 1:
                oddListHead.next = currentNode
                oddListHead = currentNode
            else:
                evenListHead.next = currentNode
                evenListHead = currentNode
            currentNode = currentNode.next
            i+=1

        # Manually terminate the even list
        evenListHead.next = None

        # Link evenList to the end of oddList
        oddListHead.next = evenListRoot
        return oddListRoot



class Test(unittest.TestCase):
    cases = [
        ([1,2,3,4,5,None], [1,3,5,2,4,None]),
        ([2,1,3,5,6,4,7,None], [2,3,6,7,1,5,4,None])
    ]

    def test0(self):
        for given, expected in self.cases:
            # Construct the root node
            # print(f"Inserting: {given[0]}")
            rootNode = ListNode(given[0])
            currentNode = rootNode

            # Construct the given linked list
            for i in range(1, len(given)-1):
                nextNode = ListNode(given[i])
                currentNode.next = nextNode
                currentNode = nextNode
                # print(f"Inserting: {given[i]}")

            print(f"Root node of Given: {rootNode.val}")

            # Test our algo
            s = Solution()
            testRootNode = s.oddEvenList(rootNode)

            # Now check against the expected list
            print(f"Test Root node returned from algo: {testRootNode.val}")
            currentNode = testRootNode
            i = 0
            while currentNode != None:
                # print(f"Checking: {currentNode.val}")
                self.assertEqual(currentNode.val, expected[i])
                currentNode = currentNode.next
                i+=1

            print("----")

unittest.main()
