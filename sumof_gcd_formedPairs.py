class Solution(object):
    def gcdSum(self, nums):
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        n=len(nums)
        mx=nums[0]
        prefixGcd=[0]*n
        for i in range(n):
            if mx<nums[i]:
                mx=nums[i]
            prefixGcd[i]=gcd(nums[i],mx)
        left=0
        right=len(prefixGcd)-1
        prefixGcd.sort()
        sum=0
        while left<right:
            sum+=gcd(prefixGcd[left],prefixGcd[right])
            left+=1
            right-=1
        return sum

        