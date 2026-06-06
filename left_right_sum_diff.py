class Solution(object):
    def leftRightDifference(self, nums):
        l=len(nums)
        left=0
        right = l-1
        le=[0]
        ri=[0]
        suml=0
        sumr=0
        for i in range(0,l):
            if left+1!=l:
                suml+=nums[left]
                le.append(suml)
            if right-1!=-1:
                sumr+=nums[right]
                ri.append(sumr)
            left+=1
            right-=1
        diff=[]
        for i in range(0,l):
            diff.append(abs(le[i]-ri[l-1-i]))
        return diff
        