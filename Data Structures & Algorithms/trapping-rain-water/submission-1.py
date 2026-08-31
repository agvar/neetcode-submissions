class Solution:
    def trap(self, height: List[int]) -> int:
        """
        for an index i, the height of water that index can hold only depends on
        the max heights that border it to the left and right- no just the immediate left and right
        But any left and right that the max w.r.t the index location.
        And then the minimum of the left and right max- as thats the floor of the water
        Now, if the index itself has a height h, then the possible water that it can hold 
        becomes min(max(left), max(right)) - h
        """
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

