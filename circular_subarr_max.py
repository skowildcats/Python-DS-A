class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        lmin = lmax = 0
        gmin = inf
        gmax = -inf
        arr_sum = 0

        for i, val in enumerate(nums):
            lmax = max(lmax + val, val)
            gmax = max(lmax, gmax)
            lmin = min(lmin + val, val)
            gmin = min(lmin, gmin)
            arr_sum += val

        if gmax > 0:
            return max(arr_sum - gmin, gmax)
        else:
            return gmax


# runtime complexity: O(n)
# space complexity: O(1)
# variation of kadane's algorithm, arr_sum - gmin = max sum crossing boundaries
# else statement catches case when all numbers are negative