class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n = len(word1)
        m = len(word2)
        l = n + m
        j = k = 0
        for i in range(l):
            if i % 2 == 0 and j < n:
                ans += word1[j]
                j += 1
                print("1")
            elif i % 2 == 1 and k < m:
                ans += word2[k]
                k += 1
                print("2")
        for j in range(j,n):
            ans += word1[j]
            i += 1
        for k in range(k,m):
            ans += word2[k]
            k += 1
        return ans