class Solution(object):
    def isValid(self, s):
        lst = []
        for i in s:
            if i==")":
                if lst and lst.pop()=="(":
                    continue
                else:
                    return False
            elif i=="]": 
                if lst and lst.pop()=="[":
                    continue
                else:
                    return False
            elif i=="}":
                if lst and lst.pop()=="{":
                    continue
                else:
                    return False
            lst.append(i)
        if len(lst)>=1:
            return False
        else:
            return True

        