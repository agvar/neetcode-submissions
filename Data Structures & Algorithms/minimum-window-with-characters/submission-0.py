class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        The logic to use a window, increasing right till valid
        then decreasing left till invalid to find the minimum length
        a window bounded by index left and index right has a lenght of (right- left + 1)
        """
        
        dict_t = defaultdict(int)
        window = defaultdict(int)
        right, left = 0,0
       
        for char in t:
            dict_t[char] += 1
        need, has = len(dict_t.keys()), 0
        min_length, min_window = float('INF'),[-1,-1]

        for right in range(len(s)):
            char_right = s[right]
            window[char_right] += 1
            if char_right in dict_t and dict_t[char_right] == window[char_right]:
                has += 1 


            while has == need and left < len(s):
                char_left = s[left]
                if right- left +1 < min_length:
                    min_window = [left, right]
                    min_length = min(min_length,right - left +1)
                window[char_left] -= 1
                left += 1 
                if char_left in dict_t and dict_t[char_left] > window[char_left]:
                    has -= 1 
            l,r = min_window
        return s[l:r+1] if min_length != float('INF') else ""

            

        
        
        