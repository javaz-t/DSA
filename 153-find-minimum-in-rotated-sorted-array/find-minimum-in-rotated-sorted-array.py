class Solution(object):
    def findMin(self, nums):

        middle =len(nums)//2

        left, right =0,len(nums)-1

        result=nums[0]

        while left<=right: 
            
            if nums[left] <= nums[right]: #one case only .happen   when list  is in sorted 
                result= min(result, nums[left])
                break

            middle =(left+right)//2
            result=min(result,nums[middle])

            #left sorted 
            if nums[middle]>=nums[left]:
                left =middle+1
            else:
                right=middle-1


        return result

            
            
        

         