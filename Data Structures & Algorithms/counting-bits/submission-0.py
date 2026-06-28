class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            j = i
            while i > 0:
                if i & 1:
                    ans[j] += 1
                    i = i >> 1
                else:
                    i = i >> 1
        return ans

        