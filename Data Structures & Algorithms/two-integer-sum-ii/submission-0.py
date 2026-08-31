class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_nums = defaultdict(int)
        for i,num in enumerate(numbers):
            if target-num in dict_nums:
                return [dict_nums[target-num]+1,i+1]
            else:
                dict_nums[num] = i
        
        