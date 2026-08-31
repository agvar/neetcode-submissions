class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        The logic here is to use left and right pointers.
        calculate the area of the first and last walls
        then move to the direction of the smaller height- meaning keep the bigger height wall the same
        """
        left = 0
        right = len(heights)-1
        area_max =0
        while left < right:
            area_curr = (right - left) * min (heights[left],heights[right])
            area_max = max(area_max,area_curr)
            if heights[left] < heights[right]:
                left +=1 
            else:
                right -=1
        return area_max



        