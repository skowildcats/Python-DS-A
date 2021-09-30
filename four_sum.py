class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        n = len(nums1)
        d1 = defaultdict(int)
        for i in range(n):
            for j in range(n):
                d1[nums1[i] + nums2[j]] += 1
        return sum(d1[-c-d] for c in nums3 for d in nums4)

# n = length of array
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)