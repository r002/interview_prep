from base.question import *

class Algo102(Question):

    description = "102) Given a linked list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time and only use constant space."

    def __init__(self):
        # numbers = [3, 3, 2, 1, 3, 2, 1]
        numbers = [1, 2, 3, 3, 2, 1, 3, 2, 1]
        # numbers = [2, 1, 3, 3, 2, 1, 3, 2, 1]
        # numbers = [2, 1, 3, 3, 1, 3, 2, 1]
        # numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        print(f"\nOriginal: {numbers}\n")

        # Dump the array into a linked list
        start_node = ListNode(numbers[0])
        cursor = start_node
        for i in range(1, len(numbers)):
            next_node = ListNode(numbers[i])
            cursor.next = next_node
            cursor = next_node

        rs = self.sort(start_node)
        print(f"\nSorted: {rs}")

    def sort(self, start_node):
        # Set up three dummy nodes represent 1, 2, 3
        node101_cursor = None
        node102_cursor = None
        node103_cursor = None

        # We need to know where chain 1 ends and where
        # chain 2 ends
        node101_end = None
        node102_end = None

        # Walk the linked list and connect each node to the
        # node chain it belongs to
        node = start_node
        while node != None:
            true_next = node.next
            # Relink the nodes to the node chains
            if node.val == 1:
                if node101_cursor is None:
                    node101_end = node
                node.next = node101_cursor
                node101_cursor = node
            elif node.val == 2:
                if node102_cursor is None:
                    node102_end = node
                node.next = node102_cursor
                node102_cursor = node
            elif node.val == 3:
                node.next = node103_cursor
                node103_cursor = node
            node = true_next

        # Link the three chains together
        node101_end.next = node102_cursor
        node102_end.next = node103_cursor

        return f"{node101_cursor.get_list()}"


class ListNode(object):
    val = None
    next = None

    def __init__(self, x):
        self.val = x

    # Function to print the list
    def get_list(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        return output
