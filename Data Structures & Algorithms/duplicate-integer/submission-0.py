class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        ans = [0]*size
        my_dict = {}
        for k in nums:
            my_dict[k] = my_dict.get(k, 0) + 1
            if my_dict[k] > 1:
                return True   
        return False