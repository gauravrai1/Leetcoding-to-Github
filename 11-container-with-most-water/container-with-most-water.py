class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        l, r = 0, len(height) -1

        # print(l,r)
        while l < r:
            # print(l,r)
            h_l = height[l]
            h_r = height[r]
            min_h = h_r
            if h_l <= h_r:
                min_h = h_l
            width = r-l
            area = min_h*width
            # print("area", area)
            if area > maxArea:
                maxArea = area

            if h_l <= h_r:
                l += 1
            else:
                r -= 1


        return maxArea