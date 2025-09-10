class Solution(object):
    def maxArea(self, height):
        total = 0    
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)  
            total = max(total, area)  
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        return total
