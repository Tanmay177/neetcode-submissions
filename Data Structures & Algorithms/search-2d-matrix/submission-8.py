class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binsearch(array: List[int], target:int) -> bool:
            left = 0
            right = len(array)-1
            while left <= right:
                mid = left + ((right-left)//2)
                if array[mid] == target:
                    return True
                elif array[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                return binsearch(matrix[i-1],target)
            elif matrix[i][0] == target:
                return True
    
        return binsearch(matrix[-1], target) 