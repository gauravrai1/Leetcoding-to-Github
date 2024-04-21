class Solution:

    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        
        area = 0

        maxL = 0
        for l,n in enumerate(height):
            maxLeft[l] = maxL
            if n > maxL:
                maxL = n
        
        maxR=0
        for r in range(len(height)-1, -1, -1):
            maxRight[r] = maxR
            if height[r] > maxR:
                maxR = height[r]
        
        # print(maxLeft, maxRight)
        for i,h in enumerate(height):
            minH = min(maxLeft[i], maxRight[i])
            currArea = minH-h
            if currArea > 0:
                area += currArea
        
        return area