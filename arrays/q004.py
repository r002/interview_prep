from base.question import *

class Arr004(Question):

    description = "4) Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time. Bonus: Use constant space."

    def __init__(self):
        # numbers = [3, 3, 2, 1, 3, 2, 1]
        # numbers = [1, 2, 3, 3, 2, 1, 3, 2, 1]
        # numbers = [2, 1, 3, 3, 2, 1, 3, 2, 1]
        numbers = [2, 1, 3, 3, 1, 3, 2, 1]
        # numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1]

        print(f"\nOriginal: {numbers}\n")
        # rs = self.sort_numbers(numbers)
        rs = self.sort_in_n_space2(numbers)
        print(f"\nSorted: {rs}")


    # This is not constant space because RS grows as a function of n.
    # To implement a constant space solution, you need to sort in-place
    # in the original array.
    def sort_in_n_space2(self, numbers):
        rs = [None] * len(numbers)
        pos_1 = 0
        pos_2 = 0
        pos_3 = len(numbers)-1
        for i in range(len(numbers)):
            if 1 == numbers[i]:
                print("Inserting: 1")
                if rs[pos_1] is not None:
                    print(f"\tPos{pos_1} occupied by {rs[pos_1]}. Shift to pos{pos_2}!")
                    rs[pos_2] = 2
                rs[pos_1] = 1
                pos_1 += 1
                pos_2 += 1
            elif 2 == numbers[i]:
                print("Inserting: 2")
                rs[pos_2] = 2
                pos_2 += 1
            elif 3 ==numbers[i]:
                print("Inserting: 3")
                rs[pos_3] = 3
                pos_3 -= 1
            print(f"RS after iteration {i+1}: {rs}")
            print(f"Cursors: {pos_1, pos_2}\n")

        return rs


    def sort_in_n_space(self, numbers):
        rs = [None] * len(numbers)
        pos_1 = 0
        quantity_2 = 0
        pos_3 = len(numbers)-1
        for i in range(len(numbers)):
            if 1 == numbers[i]:
                rs[pos_1] = 1
                pos_1 += 1
            elif 2 == numbers[i]:
                quantity_2 += 1
            elif 3 ==numbers[i]:
                rs[pos_3] = 3
                pos_3 -= 1
            print(f"RS after iteration {i+1}: {rs}")

        print(pos_1, pos_3, quantity_2)
        ## Now just dump 2s into any remaining spaces in the middle
        rs[pos_1:pos_3+1] = [2] * quantity_2

        return rs


    def sort_numbers(self, numbers):
        rs = []
        index_of_farthest_one = 0
        for i in range(len(numbers)):
            if 1 == numbers[i]:
                rs.insert(0, 1)
                index_of_farthest_one += 1
            elif 3 == numbers[i]:
                rs.append(3)
            else:
                rs.insert(index_of_farthest_one, 2)
            print(f"RS after this iteration: {rs}")
        return rs
