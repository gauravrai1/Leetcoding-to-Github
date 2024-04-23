class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        for n in nums:
            dict[n] = dict.get(n, 0) + 1
        
        for k in dict:
            if dict[k] > 1:
                return k