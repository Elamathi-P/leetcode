class Solution(object):
    def isGood(self, nums):
        nums.sort()
        maxi = nums[len(nums)-1]
        if len(nums)!= maxi+1:
            return False
        for i in range(len(nums)-2):
            if nums[i]!=i+1:
                return False
        if nums[len(nums)-2]==maxi:
            return True
        else:
            return False

        