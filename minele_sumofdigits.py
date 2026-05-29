class Solution(object):
    def minElement(self, nums):
        min=nums[0]
        for i in nums:
            sum=0
            while i>0:
                r=i%10
                sum=sum+r
                i=i//10
            if sum<min:
                min=sum
        return min
