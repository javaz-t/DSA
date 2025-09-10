class Solution(object):
    def maxArea(self, height):
        total = 0    
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)  
            total = max(total, area)  
            if height[left] > height[right]:
                area = height[right] * (right - left)  
                right = right - 1
            else:
                area = height[right] * (right - left)
                left = left + 1
        return total
