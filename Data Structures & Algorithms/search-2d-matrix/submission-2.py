class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix)
        l = 0
        r = length - 1
        inside_len = len(matrix[r]) - 1
        while l < r:
            if matrix[r][0] > target:
                r -= 1
            elif matrix[l][inside_len] < target:
                l += 1
            else:
                break
        for i in range(len(matrix[l])):
            if matrix[l][i] == target:
                return True
        return False
        
