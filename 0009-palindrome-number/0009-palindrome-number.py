class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        rev = x[::-1]
        if int(x) == int(rev):
            return True
        return False