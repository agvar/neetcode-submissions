class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [None]*len(height)
        max_right = [None] * len(height)
        
        max_left[0] = 0
        max_right [-1] = 0
        max_water = 0

        max_val = 0
        for i in range(1,len(height)):
            max_val = max(height[i-1],max_val)
            max_left[i] = max_val

        max_val =0
        for i in range(len(height)-2,-1,-1):
            max_val = max(height[i+1],max_val)
            max_right[i] = max_val

        for i in range(0,len(height)):
            max_water += max(min(max_left[i],max_right[i]) - height[i],0)
        return max_water

