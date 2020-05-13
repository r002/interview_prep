import unittest

# Source: https://leetcode.com/problems/single-element-in-a-sorted-array
# Assumptions: nums is guaranteed to not be an empty list.

class Solution:
    def singleNonDuplicate(self, nums:list) -> int:
        # Manually handle edge case
        if len(nums) == 1:
            return nums[0]

        for i in range(0, len(nums)-1, 2):
            # print(f"Index: {i} | Comparing: {nums[i]} : {nums[i+1]}")
            if nums[i]^nums[i+1] != 0:
                return nums[i]

        return nums[-1]  # Last number is the unique one! Only way to get this far in the algo.


class Test(unittest.TestCase):
    cases = [
        ([99], 99),
        ([1,2,2,3,3], 1),       # Test leftmost
        ([1,1,2,3,3], 2),
        ([1,1,999], 999),       # Test rightmost with triple
        ([1,1,2,2,3], 3),       # Test rightmost
        ([1,1,2,3,3,4,4,8,8], 2),
        ([3,3,7,7,10,11,11], 10)
    ]
    s = Solution()

    def test(self):
        for nums, expected in self.cases:
            rs = self.s.singleNonDuplicate(nums)
            print(f"{nums} | {rs} | {expected}")
            print("---")
            self.assertEqual(expected, rs)


unittest.main()
