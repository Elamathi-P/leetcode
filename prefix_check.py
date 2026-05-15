class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        first = strs[0]
        last = strs[len(strs)-1]
        i=0
        while i<len(first) and i<len(last):
            if first[i]!=last[i]:
                break
            i+=1
        return first[:i] 