class Solution(object):
    def maxSubArray(self, nums):
        total = nums[0]
        sum =0
        for n in nums:
            if sum<0:
                sum =0
            sum+=n
            total =max(sum,total)
        
        return total
        
        