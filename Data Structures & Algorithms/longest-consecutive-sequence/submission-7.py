class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        curr_seq = None
        output = 0
        len_seq = 0
        for num in nums:
            if num-1 not in nums_set:
                len_seq +=1
                while num + len_seq in nums_set:
                    len_seq +=1
                output= max(output,len_seq)
                len_seq =0
        return output

            


        