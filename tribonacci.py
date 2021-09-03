class Solution:

    cache = {}

    def tribonacci(self, n: int) -> int:

        if n in self.cache:
            return self.cache[n]

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            ans = self.tribonacci(
                n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.cache[n] = ans
        return ans


# Time Complexity: O(n)
# Space Complexity: O(n)