class Solution(object):
    def maxArea(self, height):
        total = 0    
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] > height[right]:
                area = height[right] * (right - left)  
                right -= 1
            else:
                area = height[left] * (right - left)
                left +=  1
            total =max(total,area)
        return total
