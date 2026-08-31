class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result= []
        nums.sort()
        for idx,num in enumerate(nums):
            if idx > 0 and (nums[idx] == nums[idx -1]):
                continue
            left = idx  + 1
            right = len(nums) - 1
            while (left<right):
                sum = num + nums[right] + nums[left]
                if sum == 0:
                    result.append([num,nums[left],nums[right]])
                    left += 1
                    while left<right and nums[left] == nums[left-1]:
                        left +=1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return result

        