class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coin = 0
        sorted_pile = sorted(piles)
        for i in range(len(sorted_pile) - 2, (len(sorted_pile) // 3) - 1, -2):
            coin += sorted_pile[i]
        return coin
