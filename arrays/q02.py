from base.question import *

class Arr002(Question):

    description = "2) Find the median of two sorted arrays."

    def __init__(self):
        arr1 = [1, 3, 5, 7, 13, 15, 99]
        arr2 = [2, 4, 5, 6]

        print("Original arrays:")
        print(arr1)
        print(arr2)

        # IRL implementation
        # self.irl_impl(arr1, arr2)
        self.custom_impl(arr1, arr2)


    def irl_impl(self, arr1, arr2):
        merged_arr = arr1 + arr2
        print(f"Merged original: {merged_arr}")
        merged_arr.sort()
        print(f"Merged sorted: {merged_arr}")
        median = np.median(merged_arr)
        print(f"Median of merged: {median}")


    def custom_impl(self, arr1, arr2):
        # For a basic sanity check, print no of expected items
        print(f"Total no of expected items: {len(arr1)+len(arr2)}")


        # First, merge the two arrays
        rs = []

        arr1cursor = 0
        arr2cursor = 0
        while True:
            arr1Num = arr1[arr1cursor]
            arr2Num = arr2[arr2cursor]

            if arr1Num < arr2Num:
                rs.append(arr1Num)
                arr1cursor += 1
            elif arr2Num < arr1Num:
                rs.append(arr2Num)
                arr2cursor += 1
            else:
                rs.append(arr1Num)
                rs.append(arr2Num)
                arr1cursor += 1
                arr2cursor += 1

            # Code the exit condition
            if(arr1cursor == len(arr1)):
                # We've reached the end of arr1.
                # Just dump the rest of arr2 into the rs
                rs.extend(arr2[arr2cursor:])
                break;
            elif(arr2cursor == len(arr2)):
                # We've reached the end of arr2.
                # Just dump the rest of arr1 into the rs
                rs.extend(arr1[arr1cursor:])
                break;

        print(f"Merged Array: {rs}")
        print(f"Merged size: {len(rs)}")


        # Second, find the median in the merged array

        # print(f"Median: {self.median(arr1, arr2)}")
