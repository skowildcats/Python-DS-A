class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start = 0
        end = len(s)
        res = []

        for char in s:
            if char == "I":
                res.append(start)
                start += 1
            else:
                res.append(end)
                end -= 1
        res.append(start)
        return res
