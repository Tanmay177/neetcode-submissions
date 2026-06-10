class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l,r):
            while l < r:
                if s[l]!=s[r]:
                    return False
                l +=1
                r -=1
            return True

        count = 0
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right] and count == 0:
                if isPalindrome(left+1, right):
                    left +=1
                    count = 1
                elif isPalindrome(left,right-1):
                    right -= 1
                    count = 1
                else:
                    print(s[left], s[right])
                    print("1")
                    return False
            elif s[left] == s[right]:
                left +=1
                right -=1
            elif s[left] != s[right] and count == 1:
                print(s[left], s[right])
                print("2")
                return False
        return True


        