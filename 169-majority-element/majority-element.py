 

class Solution:
    def majorityElement(self, nums):
        mE=-1
        count =-1
        for x in nums:
            if mE==x:
                count+=1
            else:
                
                if count <1:
                    mE=x
                    count =0
                else:
                    count-=1
        return mE
         
         
 