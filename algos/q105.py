from base.question import *

class Algo105(Question):

    description = "105) Reverse a singly linked list into a doubly linked list."

    def __init__(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Convert this list into a singly linked list
        start = cursor_node = ListNode(list[0])
        for i in range(1, len(list)):
            current_node = ListNode(list[i])
            cursor_node.next = current_node
            cursor_node = current_node
        end = cursor_node
        print(f"Original ll: {self.get_ll(start)}")

        reversed_ll_start = self.reverse(start)
        print(f"reversed_ll: {self.get_ll(reversed_ll_start)}")


    # Reverse the singly linked list into a doubly linked list
    # Return the start node of the doubly linked list
    def reverse(self, start):
        s_node = start
        cursor_node = ListNode2w(s_node.val)
        s_node = s_node.next
        while s_node is not None:
            d_node = ListNode2w(s_node.val)
            d_node.next = cursor_node
            cursor_node.previous = d_node
            cursor_node = d_node
            s_node = s_node.next

        return cursor_node


    def get_ll(self, start):
        list = []
        node = start
        while node is not None:
            list.append(node.val)
            node = node.next
        return list


class ListNode(object):
    val = None
    next = None

    def __init__(self, x):
        self.val = x


class ListNode2w(object):
    val = None
    next = None
    previous = None

    def __init__(self, x):
        self.val = x
