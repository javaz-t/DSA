class Solution(object):
    def productExceptSelf(self, nums): 
        result=[] 
        for i in range( len(nums)):          
            val=1 if i==0 else val*nums[i-1]
            result.append(val)
        post=1
        for i in range( len(nums)-1,-1,-1):
            val=post*result[i] if i==len(nums)-1 else post*result[i]*nums[i+1]
            if i!=len(nums)-1:
                post*=nums[i+1]
            result[i]=val
        return result
        
         
        
             
                    
print(Solution().productExceptSelf([1,2,3,4]))