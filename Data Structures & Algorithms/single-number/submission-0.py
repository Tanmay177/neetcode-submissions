class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pro = 0
        for i in nums:
            pro = pro^i
        return pro
        