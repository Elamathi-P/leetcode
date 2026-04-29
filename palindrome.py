class Solution(object):
    def isPalindrome(self, x):
        r=str(x)
        s = r[::-1]
        if(s==r):
            return True
        else:
            return False
        