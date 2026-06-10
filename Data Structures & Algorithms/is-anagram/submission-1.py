class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        for item in s:
            freq1[item] = freq1.get(item, 0) + 1
        freq2 = {}
        for item in t:
            freq2[item] = freq2.get(item, 0) + 1
        if freq1 == freq2:
            return True        
        return False