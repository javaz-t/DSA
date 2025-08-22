class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]        # start with first element
        max_sum = nums[0]            # initialize max with first element

        for num in nums[1:]:         # iterate from second element
            # Decide: extend current subarray OR start fresh
            current_sum = max(num, current_sum + num)
            # Update global max
            max_sum = max(max_sum, current_sum)

        return max_sum

        
        