class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # def binSearch( nums: List[int], target:int) -> int:
        #     left = 0
        #     right = len(nums)-1

        #     while left < right:
        #         mid = left + ((right-left)//2)
        #         if nums[mid] == target:
        #             return mid
        #         elif nums[mid] < target:
        #             left = mid+1
        #         elif nums[mid] > target:
        #             right = mid 
        #     return None
        
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue;
            left = i + 1
            right = len(nums)-1
            target = nums[i]*-1
            while left < right:
                if nums[left] + nums[right] == target:
                    ans.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        
        list1 = list()
        for t in ans:
            list1.append(t)
        return list1



            # for j in range(i+1,len(sorted_Nums)):
            #     target1 = (sorted_Nums[i] + sorted_Nums[j])*(-1)
            #     third = binSearch(sorted_Nums, target1)
            #     if third != None:
            #         ans.append([sorted_Nums[i],sorted_Nums[j],sorted_Nums[third]])



        