class Solution(object):
    def containsDuplicate(self, nums):
        #set use to remove the duplicate items 
        setCount=set(nums)
        #checkign the values lenth are same or not 
        return len(setCount)!=len(nums)
        