class Solution(object):
   def containsDuplicate(self,nums):
    
        # #set use to remove the duplicate items 
        # setCount=set(nums)
        # #checkign the values lenth are same or not 
        # return len(setCount)!=len(nums)
    l,r =(0,1)
    nums.sort()
    if len(nums)==1:
        return False
    while(r<len(nums)):
        if nums[l]==nums[r]:
            return True
        else:
            l+=1
            r+=1
    return False
        