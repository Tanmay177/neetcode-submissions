class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join([char for char in s if char.isalnum()])
        print(t)
        t = t.lower()
        print(t)
        left = 0
        right = len(t) - 1
        while left < right:
            if t[left] != t[right]:
                return False
            else:
                left +=1
                right -=1
        return True
        