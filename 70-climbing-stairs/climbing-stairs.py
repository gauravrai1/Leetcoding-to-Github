class Solution:
    def climbStairs(self, n: int) -> int:
        def climbStairsMemo(n: int, memo: dict) -> int:
            if n in memo:
                return memo[n]
            if n == 0 or n == 1:
                return 1
            ways = climbStairsMemo(n-1, memo) + climbStairsMemo(n-2, memo)
            memo[n] = ways
            return ways
        return climbStairsMemo(n, {})