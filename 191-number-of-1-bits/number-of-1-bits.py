class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        setbit = 0
        for b in binary:
            if b == "1":
                setbit += 1
        return setbit