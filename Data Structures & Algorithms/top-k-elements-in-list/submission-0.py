class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = defaultdict(int)
        for num in nums:
            dict_nums[num] += 1
        sorted_dict_nums = dict(sorted(dict_nums.items(), key=lambda x:x[1], reverse=True))
        return list(sorted_dict_nums.keys())[0:k]
        