class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        calculate the max occuring character in a window
        count of non-max chars meeds to be <= k
        the window length(total chars) = right - left + 1
        window length - max char length <= k
        if the window is valid- increase right by 1
        if window is invalid- increase left by 1
        """
        char_freq = defaultdict(int)
        right, left = 0,0
        max_freq = 0
        max_length = 0
        for right in range(len(s)):
            char_freq[s[right]] += 1
            max_freq = max(max_freq,char_freq[s[right]])
            if (right - left + 1) - max_freq > k :
                char_freq[s[left]] -= 1
                left += 1
            max_length = max(max_length,right - left + 1)
                
        return max_length

        






        