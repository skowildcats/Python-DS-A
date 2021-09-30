class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row = 0

        for i in range(m):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                row = i
                break

        for i in range(n):
            if matrix[row][i] == target:
                return True

        return False
