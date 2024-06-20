class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = sys.maxsize
        while l <= r:
            mid = l + ((r-l) // 2)

            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

            if nums[mid] < res:
                res = nums[mid]

        return res