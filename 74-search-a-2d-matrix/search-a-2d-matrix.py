class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row search
        t, b = 0, len(matrix)-1
        col = []

        while t <= b:
            mid = t + ((b - t) // 2)
            if target > matrix[mid][-1]:
                t = mid + 1
            elif target < matrix[mid][0]:
                b = mid - 1
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                col = matrix[mid]
                break
        
        if len(col) == 0:
            return False
        
        # column search
        l, r = 0, len(col) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if target > col[mid]:
                l = mid + 1
            elif target < col[mid]:
                r = mid - 1
            
            if target == col[mid]:
                return True
        
        return False