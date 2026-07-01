import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + ((hi-lo)//2)
            sum1 = 0
            for p in piles:
                sum1 += math.ceil(p/mid)
            if sum1 <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo