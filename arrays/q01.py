from base.question import *

class Arr001(Question):

    description = "1) Find the average of the median of two sorted arrays."

    def __init__(self):
        arr1 = [1, 3, 5, 7]
        arr2 = [2, 4, 6]
        print(f"Avg of Median: {self.median(arr1, arr2)}")

    def median(self, arr1, arr2):
        median = None

        # Numpy implementation - How I'd do it IRL
        med1 = np.median(arr1)
        med2 = np.median(arr2)
        median = np.median([med1, med2])

        # Custom implementation - How they might ask me to do it?
        med1 = self.find_median(arr1)
        med2 = self.find_median(arr1)
        median = self.find_median([med1, med2])

        return median

    def find_median(self, arr):
        # If it's an odd-sized set, just take the middle number
        if 1 == len(arr) % 2:
            middle_pos = math.floor(len(arr)/2)  # 0 |1| 2
            return arr[middle_pos]

        # If it's an even-sized set, we need to average the middle
        # two numbers
        else:
            middle_pos_l = len(arr)//2-1  # 0 |1| 2 3
            middle_pos_r = len(arr)//2    # 0 1 |2| 3
            median = (arr[middle_pos_l]+arr[middle_pos_r])/2
            return median
