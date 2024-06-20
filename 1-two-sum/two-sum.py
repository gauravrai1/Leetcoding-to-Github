class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i, n in enumerate(nums):
            required = target - n
            if required in hashmap.keys():
                return [i, hashmap[required]]
            else:
                hashmap[n] = i