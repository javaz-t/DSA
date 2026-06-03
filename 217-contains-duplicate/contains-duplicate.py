class Solution(object):
    def containsDuplicate(self, nums):
       hashMap ={}
       for i,x in enumerate(nums):
            if x in hashMap:
                return True
            else:
                hashMap[x]=i
       return False