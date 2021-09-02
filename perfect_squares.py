def numSquares(self, n: int) -> int:
  dp = [i for i in range(n+1)]

  for i in range(n + 1):
      j = 1

      while j*j <= i:
          dp[i] = min(dp[i], dp[i - (j*j)] + 1)
          j += 1
  return dp[-1]


# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
