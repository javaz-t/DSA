class Solution(object):
    def productExceptSelf(self, nums):
        prefix=[]
        postfix=[]
        result=[]
        val=1

        for i in range( len(nums)):
            val=val*nums[i]
            prefix.append(val)
        #print(prefix)
        val=1
        for i in range(len(nums)-1,-1,-1):
            val=val*nums[i]
            postfix.insert(0, val)
        #print(postfix)
        
        for i in range(len(nums)):
            prefixVal = 1 if i == 0 else prefix[i - 1]
            postfixVal = 1 if i == len(nums) - 1 else postfix[i + 1]
            result.append(prefixVal * postfixVal)
        #print(result)
        return result