class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        letters = defaultdict(int)
        seen = defaultdict(str)
        count = 0
        res = 0

        for char in croakOfFrogs:
            if char == "c":
                count += 1
                res = max(res, count)
            elif char == "k" and count > 0:
                count -= 1

            letters[char] += 1
            seen[letters[char]] += char

        for word in list(seen.values()):
            if word != "croak":
                return -1
        return res
