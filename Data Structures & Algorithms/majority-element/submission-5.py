class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        floor = len(nums)/2
        print(floor)
        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        
        for n in hash_map:
            if hash_map[n] > floor:
                print
                return n