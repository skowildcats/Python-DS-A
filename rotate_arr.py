class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0:
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        """
        Do not return anything, modify nums in-place instead.
        """

# Time Complexity: O(n)
# Space Complexity: O(n)