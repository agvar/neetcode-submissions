class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        The solution involves having a right and left pointer
        the left pointer defining the window start and right defining the end
        a unique substring is made up all unique chars
        The moment the substring becomes non-unique, the current char is dup
        So we change the window start to the first occurance of the dup char
        """
        left = 0
        right = 0
        max_length = 0 
        substr = dict()
        while right < len(s):
            if s[right] in substr:
                left = max(left,substr.get(s[right]) + 1 )
                substr[s[right]] = right
                max_length = max(max_length,right - left + 1)
            else:
                substr[s[right]] = right
                max_length = max(max_length,right - left + 1)
            right += 1
        return max_length

            

                
            
            
        