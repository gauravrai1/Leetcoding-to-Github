class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # range of k
        piles = sorted(piles)
        l = 1
        r = piles[-1]

        res = l
        while l <= r:
            k = l + ((r-l) // 2)

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                                    
            if hours > h:
                l = k + 1
            elif hours <= h:
                r = k - 1

            if h >= hours:
                res = k
        return res