 

class Solution:
    def majorityElement(self, nums):
        result = {}
        for   x in  nums :
            if x in result:
                result[x] = result[x] + 1
            else:
                result[x] = 1
        return max(result,key=result.get)

 