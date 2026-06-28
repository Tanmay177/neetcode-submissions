class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans1, ans2 = 0,0

        for i in range(n+1):
            ans2 = ans2^i
        for i in nums:
            ans1 = ans1^i
            
        return ans1^ans2