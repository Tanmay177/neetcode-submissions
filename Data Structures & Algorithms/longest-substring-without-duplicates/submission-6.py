class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s) #8
        charSet = set()
        i = 0

        maxL = 0
        
        for j in range(len(s)):
                while s[j] in charSet:
                    charSet.remove(s[i])
                    i += 1
                charSet.add(s[j])
                maxL = max(maxL, j-i+1)
        return maxL
