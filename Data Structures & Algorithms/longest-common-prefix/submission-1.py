class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0 
        min1 = float('inf')
        for n in strs:
            if len(n) < min1:
                min1 = len(n)


        for i in range(min1):
            prefix += strs[0][i]
            for n in strs:
                print(n[i] ,prefix[i])
                if n[i] != prefix[i]:
                    return prefix[0:i]
        
        return prefix        
                
        