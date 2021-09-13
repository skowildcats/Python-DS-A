class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = {}
        max_seen = 0
        res = []
        count = 0

        for i, char in enumerate(s):
            seen[char] = i
        for i, char in enumerate(s):
            max_seen = max(max_seen, seen[char])
            count += 1
            if i == max_seen:
                res.append(count)
                count = 0

        return res
