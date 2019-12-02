# import arrays.q001               # This works
# print(q001.Arr001.description)

# from arrays.q001 import *        # This also works
# print(Arr001.description)


greetings = "Hello there!"
s = f"""
Greeting message: {greetings}
"""
print(s)

ll = [1, 2, 3, 4, 5]
s = "".join(map(str, ll))
print(s)
print()

## Lambda Functions
##
l = map(lambda x : x*2, ll)
print(list(l))
print()

add = lambda x, y : x + y
print(add(2, 3))
print()

# def test_append(foo):
#     bar = foo
#     bar.append(999)
#
# list = [1, 2, 3]
# print(f"List before: {list}")
# test_append(list)
# print(f"List after: {list}")
#
# if not None:
#     print("Print not None")

class Node(object):
    val = None
    next = None

    def __init__(self, x):
        self.val = x

def print_ll(head_node):
    l = []
    node = head_node
    while node is not None:
        l.append(node.val)
        node = node.next
    print(f"list: {l}")

def reverse_ll(head_node):
    #Initializing values
    prev = None
    curr = head_node  # Node0
    next = curr.next  # Node1

    #looping
    while curr:
        #reversing the link
        curr.next = prev

        #moving to next node
        prev = curr
        curr = next
        if next:
            next = next.next

    # Return the head node of the reversed list
    return prev

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

print("Original:")
print_ll(node1)
head_node = reverse_ll(node1)
print("Reversed:")
print_ll(head_node)
