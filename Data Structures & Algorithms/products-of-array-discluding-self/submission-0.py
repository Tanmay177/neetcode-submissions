class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        product = 1
        prefix = [1]*n
        for i in range(len(nums)):
            product = product*nums[i]
            prefix[i] = product
        
        product = 1
        suffix = [1]*n
        for i in range(len(nums)-1,-1,-1):
            print(i)
            product = product*nums[i]
            suffix[i] = product
        prefix.insert(0,1)
        suffix.insert(n,1)
        print(prefix)
        print(suffix)

        nums2 = [1]*n

        for i in range(len(nums2)):
            nums2[i] = prefix[i]*suffix[i+1]
     
        
        return nums2
        