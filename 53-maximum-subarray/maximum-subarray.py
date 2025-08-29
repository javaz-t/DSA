class Solution(object):
    def maxSubArray(self, nums):
        total = 0
        sum =0
        if(len(nums)==1):
            return nums[0]
        if all(n<0 for n in nums):
            return max(nums)
        for i in range(0,len(nums) ):
            if(i==0):
                total=nums[0]
            sum+=nums[i]
            if(sum<0):
                sum=0
            if(sum>total):
                total=sum
        return total
        
        