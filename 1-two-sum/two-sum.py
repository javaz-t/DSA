class Solution(object):
    def twoSum(self, nums, target):
        seen ={}
        for i,n in enumerate(nums):
            needVal = target-n
            if needVal in seen:              
                return [seen[needVal], i]     
            seen[n] = i 
        return [0,0]
        