from base.question import *

class Arr003(Question):

    description = "3) Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found."

    def __init__(self):
        # numbers = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
        # numbers = [1, 3, 3, 5, 7, 8, 9, 9, 15]
        # numbers = [9]
        numbers = [1, 2, 3]
        target = 9

        print(f"Numbers: {numbers}")
        print(f"Target: {target}")

        try:
            rs = self.find_range(numbers, target)
        except:
            rs = -1, -1

        print(f"\nAnswer: {rs}")


    def find_range(self, numbers, target):
        first_index = numbers.index(target)
        last_index = len(numbers) - numbers[::-1].index(target) - 1

        return first_index, last_index
