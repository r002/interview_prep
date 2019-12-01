from base.question import *

class Algo106(Question):

    description = "106) You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.  Evaluate in a single pass of the list."

    def __init__(self):
        list = [7, 4, 0, -3, 2, 1]
        k = 100
        print(f"List: {list}")
        print(f"k: {k}\n")
        rs = self.two_sum(list, k)


    def two_sum(self, list, k):
        while len(list) > 1:
            list2 = list[1:]
            for num in list:
                for num2 in list2:
                    if k == num + num2:
                        print(f"Success! {num} | {num2}")
                        return True
            list.pop(1)
        print(f"Fail! No combo produces {k}")
        return False
