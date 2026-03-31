#Was it a car or a cat I Saw
#l                         r
#alphanumeric chars: uppercase, lowercase, or num
class Solution:
    #create a function that determines whether a char is valid
    def isAlpha(self, s: str) -> bool:
        return (ord('a') <= ord(s) <= ord('z') or
                ord('A') <= ord(s) <= ord('Z') or
                ord('0') <= ord(s) <= ord('9'))
    
    def isPalindrome(self, s:str) -> bool:
        l = 0
        r = len(s) -1
        while l < r:
            while l < r and not self.isAlpha(s[l]): #removes non ASCII printable chars
                l += 1
            while l < r and not self.isAlpha(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        

        