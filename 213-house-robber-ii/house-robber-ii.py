class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 3:
            return max(nums)

        # max from 0, n-1
        temp = nums[:len(nums)-1]
        maxval = temp[-1]
        for i in range(len(temp)-3, -1, -1):
            temp[i] += maxval
            maxval = max(maxval, temp[i+1])
        max1 = max(temp[0], temp[1])

        # max from 1, n
        temp = nums[1:]
        maxval = temp[-1]
        for i in range(len(temp)-3, -1, -1):
            temp[i] += maxval
            maxval = max(maxval, temp[i+1])
        max2 = max(temp[0], temp[1])

        return max(max1, max2)