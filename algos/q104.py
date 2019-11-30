from base.question import *

class Algo104(Question):

    description = "104) Convert a list to a doubly linked list."

    def __init__(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        start, end = self.convert_list_to_dll(list)
        print(f"Original:\t{list}")
        print(f"DLL Fwd:\t{start.walk_and_print_forward()}")
        print(f"DLL Bkwd:\t{end.walk_and_print_backward()}")

    # Convert a list to a doubly linked list
    # Return (start_node, end_node)
    def convert_list_to_dll(self, list):
        start = cursor_node = ListNode2W(list[0])
        for i in range(1, len(list)):
            current_node = ListNode2W(list[i])
            cursor_node.next = current_node
            current_node.previous = cursor_node
            cursor_node = current_node

        return start, cursor_node



# A two-way node for a doubly linked list
class ListNode2W(object):
    val = None
    next = None
    previous = None

    def __init__(self, x):
        self.val = x

    def walk_and_print_forward(self):
        node = self
        list = []

        while node is not None:
            list.append(node.val)
            node = node.next

        return list

    def walk_and_print_backward(self):
        node = self
        list = []

        while node is not None:
            list.append(node.val)
            node = node.previous

        return list
