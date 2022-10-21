class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        left = 0
        right = col
        cur_row = 0
        
        while cur_row < row:
            if target > matrix[cur_row][-1]:
                cur_row += 1
                continue
            
            if target < matrix[cur_row][0]:
                return False
            
            while right > left:
                mid = (left + right)//2
                if matrix[cur_row][mid] > target:
                    right = mid
                elif matrix[cur_row][mid] < target:
                    left = mid + 1
                else:
                    return True
            
            return False
