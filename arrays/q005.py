from base.question import *

class Arr005(Question):

    description = "5) You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value. We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n)."

    # [13, 4, 7]  # True
    # [13, 4, 1]  # False
    # Translation: Basically, list[n] > list[n+1] at most once

    def __init__(self):
        test_cases = [
            ([13, 4, 7], True),
            ([13, 5, 1], False),
            ([2, 2, 2, 2, 2], True),
            ([1, 2, 2, 2, 2], True),
            ([3, 2, 2, 2, 2], True),
            ([5, 3, 2, 2, 2], False),
            ([50, 200, 50, 50, 75], True),
            ([100, 50, 200, 50, 50, 75], False)  # Returns false bc you need to change two numbers to make this list non-decreasing
        ]
        all_pass = True
        df = pd.DataFrame(columns=['Test','Expected','Result','Test_Pass'])
        i = 0
        for test in test_cases:
            rs = self.check(test[0])
            test_pass = rs == test[1]
            # print(f"Test: {test[0]} | {test[1]} | {rs}\n")
            df.loc[i] = [test[0], test[1], rs, test_pass]
            if test_pass == False : all_pass = False
            i += 1

        print(df)
        print(f"\nTest Suite Result: {all_pass}")

    def check(self, alist):
        # print(f"Original list: {alist}")
        modifications = 0
        for i in range(len(alist)-1):
            if alist[i+1] < alist[i]:
                modifications += 1

        if modifications < 2:
            # print(f"Success! Mods made: {modifications}")
            return True
        else:
            # print(f"Failure! Mods made: {modifications}")
            return False

    # # Checks to see if all items in this list are non-decreasing
    # # If a single item increases, immediately return False
    # def check_if_nd(self, alist):
    #     for i in range(len(alist)-1):
    #         if alist[i+1] < alist[i]:
    #             return False
    #     return True
