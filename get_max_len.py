class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for i in range(n)]

        if nums[0] > 0:
            dp[0][0] = 1
        elif nums[0] < 0:
            dp[0][1] = 1

        res = dp[0][0]

        for i in range(1, n):
            cur = nums[i]

            if cur > 0:
                dp[i][0] = dp[i-1][0] + 1
                if dp[i-1][1] > 0:
                    dp[i][1] = max(dp[i][1], dp[i-1][1] + 1)
            elif cur < 0:
                dp[i][1] = dp[i-1][0] + 1
                if dp[i-1][1] > 0:
                    dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)

            res = max(res, dp[i][0])

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)