class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        maxval = nums[-1]

        for i in range(len(nums)-3, -1, -1):
            nums[i] = maxval + nums[i]
            maxval = max(maxval, nums[i+1])
        
        return max(nums[0], nums[1])