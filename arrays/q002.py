from base.question import *

class Arr002(Question):

    description = "2) Find the median of two sorted arrays."

    def __init__(self):
        arr1 = [2, 4, 5, 6]
        # arr1 = [2, 2, 2, 2]
        # arr1 = []

        arr2 = [1, 3, 5, 7, 13, 15, 99]
        # arr2 = []

        arr1.reverse()
        # arr2.reverse()

        print("Original arrays:")
        print(arr1)
        print(arr2)

        # IRL implementation
        # self.irl_impl(arr1, arr2)

        # Custom implementation
        self.custom_impl(arr1, arr2)


    def irl_impl(self, arr1, arr2):
        merged_arr = arr1 + arr2
        print(f"Merged original: {merged_arr}")
        merged_arr.sort()
        print(f"Merged sorted: {merged_arr}")
        median = np.median(merged_arr)
        print(f"Median of merged: {median}")


    def check_if_asc(self, arr):
        if arr[0] > arr[-1]:
            return arr[::-1]  # Returns a reversed list
        return arr


    def custom_impl(self, arr1, arr2):
        rs = []

        # Perform a sanity check:
        # Is either list empty?
        if not arr1 and not arr2:
            print("Error! Both arrays are empty!")
            return None
        elif not arr1:
            rs = arr2
        elif not arr2:
            rs = arr1
        else:
            rs = self.merge_arrays(arr1, arr2)

        print(f"Merged Array: {rs}")
        print(f"(Merged size: {len(rs)})")

        # Second, find the median in the merged array
        print(f"Median: {self.find_median(rs)}")


    def merge_arrays(self, arr1, arr2):
        # Perform a sanity check:
        # Our custom_impl *only* works with the array is sorted
        # in *ascending* order.  But this may not be the case!
        # Check to see that the arrays we're given are sorted in
        # ascending order. Sort it in asc if it's not.
        arr1 = self.check_if_asc(arr1)
        arr2 = self.check_if_asc(arr2)

        # For a basic sanity check, print no of expected items
        print(f"(Total no of expected items: {len(arr1)+len(arr2)})\n")

        # First, merge the two arrays
        rs = []
        arr1cursor = arr2cursor = 0
        while arr1cursor!=len(arr1) and arr2cursor!=len(arr2):
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
            elif(arr2cursor == len(arr2)):
                # We've reached the end of arr2.
                # Just dump the rest of arr1 into the rs
                rs.extend(arr1[arr1cursor:])

        return rs

    def find_median(self, arr):
        # If the array is odd-sized, just take its middle item.
        # Eg. 0 1 |2| 3 4  # Return 2
        if 1 == len(arr) % 2:
            pos = math.floor(len(arr)/2)
            return arr[pos]
        else:
        # If the array is even-sized, we need to take the mean
        # of the middle two items.
        # Eg. 0 |1 2| 3  # Return (1+2)/2
            pos_l = len(arr)//2 - 1
            pos_r = len(arr)//2
            return (arr[pos_l] + arr[pos_r])/2
