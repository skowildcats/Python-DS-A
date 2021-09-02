def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
    c, res, l, i = Counter(barcodes), [0]*len(barcodes), len(barcodes), 0
    for k, v in c.most_common():
        for _ in range(v):
            res[i] = k
            i += 2
            if i >= l: i = 1
    return res


# Time Complexity: O(n)
# Space Complexity: O(1)
