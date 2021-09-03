class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num) % 2 != 0:
            return num
        else:
            for idx, i in enumerate(num[::-1]):
                if int(i) % 2 != 0:
                    return num[0: len(num) - idx]
            return ""

# Time Complexity: O(n)
# Space Complexity: O(1)