class Solution(object):
    def twoSum(self, nums, target):
        #[2,7,11,15], target = 9
        l,r=0,len(nums)-1
        while(l<r):
            sumVal=nums[r]+nums[l]
            if target==sumVal:
                return [l+1,r+1]
            elif target<sumVal:#9<17  <13
                r-=1
            else:
                l+=1
        return [ ]

        