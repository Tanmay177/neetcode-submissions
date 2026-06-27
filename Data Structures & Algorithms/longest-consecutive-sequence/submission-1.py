class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        hash1 = set()

        for i in nums:
            hash1.add(i)
        print(hash1)
        for i in range(len(nums)):
            print(i)
            if (nums[i]-1) not in hash1:
                long = 1
                n = 1
                while (nums[i]+n) in hash1:
                    long +=1
                    n +=1
                longest = max(longest,long)


        return longest
        