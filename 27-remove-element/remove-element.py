class Solution(object):
    def removeElement(self, nums, val):
        k=0
        result =[]
        for x in nums:
            if x==val:
                result.append('_')
            else:
                result.insert(0,x)
                k=k+1
        nums[:] = result
        return k

       