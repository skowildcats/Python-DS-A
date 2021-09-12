class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        sorted_num = sorted(nums)
        res = []

        while start < end:
            res.append(sorted_num[start] + sorted_num[end])
            start += 1
            end -= 1
        return max(res)

# Time Complexity: O(nlogn)
# Space Complexity: O(n)