class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right = [1] * len(nums)
        right_to_left = [1] * len(nums)
        output = [1] * len(nums)
        product = 1 
        for i in range(0,len(nums),1):
            product *= nums[i]
            left_to_right[i]=product
        product = 1
        for i in range(len(nums)-1,-1,-1):
            product *= nums[i]
            right_to_left[i]=product

        for i in range(len(nums)):
            if i == 0:
                output[i] = right_to_left[i+1]
            elif i == len(nums) -1:
                output[i] = left_to_right[i-1]
            else:
                output[i] = right_to_left[i+1] * left_to_right[i-1]
        return output






        