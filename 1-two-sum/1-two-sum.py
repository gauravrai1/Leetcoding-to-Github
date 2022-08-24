class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []
        og_nums = nums
        for i, num in enumerate(nums):
            for j, element in enumerate(nums[i+1:]):
                if num + element == target:
                    final.append(i)
                    final.append(j+i+1)
                    break
            if len(final) == 2:
                break
        return final
                
            