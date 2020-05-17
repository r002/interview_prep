import unittest

# Source: https://leetcode.com/problems/maximum-sum-circular-subarray

# class Solution:
#     def maxSubarraySumCircular(self, A:list) -> int:
#         B = A + A[:-1]
#         print(B)
#         return self.maxSubArray(B, len(A))
#
#     def maxSubArray(self, nums:list, original_length:int) -> int:
#         zero_is_possible = False
#         used_indices = set()
#
#         # Run Kadane's algorithm:
#         best_sum = 0
#         current_sum = best_sum
#         for i, x in enumerate(nums):
#             current_sum = max(0, current_sum + x)
#
#             if current_sum > best_sum:
#                 if i % original_length in used_indices:
#                     break
#                 best_sum = current_sum
#                 used_indices.add(i)
#             print(f"x: {x}\t| current_sum: {current_sum} | best_sum: {best_sum} | {used_indices}")
#
#             if x==0: zero_is_possible = True
#
#         # If best_sum is 0, confirm edgecase that nums aren't all negative.
#         # If nums ARE all negative, there needs to at least be a zero in nums.
#         if 0==best_sum and not zero_is_possible:
#             return max(nums)  # In this case, best_sum will be the smallest negative num in nums.
#
#         return best_sum

# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/242169/Short-Python-DP-beats-93
# Needed to look at this hint to solve. Enormously clever!
class Solution(object):
    def maxSubarraySumCircular(self, A:list)->int:
        if max(A) <= 0: return max(A)
        endmax = [i for i in A]
        endmin = [i for i in A]
        for i in range(1, len(A)):
            if endmax[i-1] > 0: endmax[i] += endmax[i-1]
            if endmin[i-1] < 0: endmin[i] += endmin[i-1]

        return max(max(endmax), sum(A)-min(endmin))


    # https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
    # Another clever solution!
    # def maxSubarraySumCircular(self, A):
    #     total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
    #     for a in A:
    #         curMax = max(curMax + a, a)
    #         maxSum = max(maxSum, curMax)
    #         curMin = min(curMin + a, a)
    #         minSum = min(minSum, curMin)
    #         total += a
    #     return max(maxSum, total - minSum) if maxSum > 0 else maxSum


class Test(unittest.TestCase):
    cases = [
        ([1,-2,3,-2], 3),
        ([5,-3,5], 10),
        ([3,-1,2,-1], 4),
        ([3,-2,2,-3], 3),
        ([-2,-3,-1], -1)  # All negatives.
    ]
    s = Solution()

    def test0(self):
        for nums, expected in self.cases:
            result = self.s.maxSubarraySumCircular(nums)
            print(f"{nums} | {result} | {expected}")
            print("---")
            self.assertEqual(result, expected)

unittest.main()
