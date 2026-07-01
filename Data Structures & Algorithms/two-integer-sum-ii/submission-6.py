class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i = 0
        # j = 1
        # while i < j and j < len(numbers):
        #     if numbers[i]+numbers[j] == target:
        #         return [i+1,j+1]
        #     elif numbers[i]+numbers[j] < target and j == len(numbers)-1:
        #         i += 1
        #     elif numbers[i]+numbers[j] < target:
        #         j += 1            
        #     elif numbers[i]+numbers[j] > target and j == len(numbers)-1:
        #         j -= 1
        #         i += 1
        #     elif numbers[i]+numbers[j] > target:
        #         i += 1
        # return None
        n = len(numbers)  
        for i in range(n-1):
            for j in range(i+1, n):
                print(i,j)
                if numbers[i]+numbers[j] == target:
                    return [i+1,j+1]
        return None