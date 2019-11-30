from base.question import *

class Algo103(Question):

    description = "103) Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?"

    def __init__(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        start, end = self.convert_list_to_sll(list)
        print(f"Original:\t{list}")
        print(f"S.Linked L:\t{start.walk_and_print()}")

        reversed_sll_start_node = self.reverse_3n(start)
        print(f"Reversed sll:\t{reversed_sll_start_node.walk_and_print()}")

    # Return the start and end nodes of this ll
    def convert_list_to_sll(self, list):
        start_node = ListNode(list[0])
        anchor = start_node  # Keep track of the start of our linked list
        for i in range(1, len(list)):
            node = ListNode(list[i])
            start_node.next = node
            start_node = node
        return anchor, node

    # Returns the start node of the reversed ll in O(3n):
    # n to convert ll into a list
    # n to reverse the list
    # n to dump the reversed array back into a ll
    # Space complexity is 2n:
    # n for the additional list
    # n for the reversed ll
    def reverse_3n(self, start_node):
        # First, put all nodes into a list
        cursor = start_node
        list = []
        while cursor is not None:
            list.append(cursor.val)
            cursor = cursor.next
        start, end = self.convert_list_to_sll(list[::-1])
        return start

    # Return the start and end nodes of this ll
    def convert_list_to_sll(self, list):
        start_node = ListNode(list[0])
        anchor = start_node  # Keep track of the start of our linked list
        for i in range(1, len(list)):
            node = ListNode(list[i])
            start_node.next = node
            start_node = node
        return anchor, node


# A node for a singly linked ll
class ListNode(object):
    val = None
    next = None

    def __init__(self, x):
        self.val = x


    def walk_and_print(self):
        node = self
        list = []

        while node is not None:
            list.append(node.val)
            node = node.next

        return list
