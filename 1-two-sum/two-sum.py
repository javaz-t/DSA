class Solution(object):
    def twoSum(self, nums, target):
        prevMap={}
        for i , x in enumerate(nums):
            diff = target -x
            if diff in prevMap:
                return [prevMap[diff],i  ]
            else:
                prevMap[x]=i
        return
