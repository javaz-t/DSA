class Solution(object):
    def twoSum(self, nums, target):
        seen ={}
        for i,n in enumerate(nums):
             if target-n in seen:              
                return [seen[target-n], i]     
             seen[n] = i 
        return [0,0]
        