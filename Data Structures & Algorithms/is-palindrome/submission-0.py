class Solution:
    def isPalindrome(self, s: str) -> bool:
        right_p = len(s) - 1
        left_p = 0
        if len(s) <= 1:
            return True
        while right_p > left_p:
            print(f'right:{s[right_p]}')
            print(f'left:{s[left_p]}')
            if not s[right_p].isalnum():
                right_p -= 1
                continue
            if not s[left_p].isalnum():
                left_p += 1
                continue
            if s[right_p].isalnum() and s[left_p].isalnum() :
                if s[right_p].upper() != s[left_p].upper():
                    return False

            right_p -= 1
            left_p += 1

        return True


        