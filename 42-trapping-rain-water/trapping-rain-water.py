class Solution:

    def trap(self, height: List[int]) -> int:
        
        area = 0
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]

        print(maxL, maxR)

        while l < r:
            print(maxL, maxR)
            if maxL < maxR:
                l += 1
                maxL = max(height[l],maxL)
                area += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r],maxR)
                area += maxR - height[r]
        
        return area