class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        res = []
        for i in range(n):
            res.append([0] * m)

        for i in range(n):
            for j in range(m):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]

        return res


#greedy algorithm
# Time Complexity: O(n*m)
# Space Complexity: O(n*m)