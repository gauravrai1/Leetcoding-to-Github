class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        replace = 0
        while i<len(nums):
            if nums[i] == "_":
                break
            if nums[i-1] == nums[i]:
                nums.remove(nums[i])
                nums.append("_")
                replace += 1
            else:
                i += 1
        return len(nums)-replace