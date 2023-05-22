# Koko Eating Bananas
## Link: https://leetcode.com/problems/koko-eating-bananas/
def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if sum((p + m - 1) // m for p in piles) > h:
                l = m + 1
            else:
                r = m
        return l
