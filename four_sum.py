class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        n = len(nums1)
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(n):
            for j in range(n):
                d1[nums1[i] + nums2[j]] += 1
                d2[nums3[i] + nums4[j]] += 1
        for k in d1.keys():
            remain = 0 - k
            if remain in d2:
                count += d1[k] * d2[remain]
        return count
