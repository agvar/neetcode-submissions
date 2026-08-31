class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for letter in s:
            dict_s[letter] += 1
        for letter in t:
            dict_t[letter] += 1
        print("dict_s",dict_s)
        print("dict_t",dict_t)

        for letter,count in dict_t.items():
            if letter not in dict_s or count != dict_s[letter]:
                return False
        for letter,count in dict_s.items():
            if letter not in dict_t or count != dict_t[letter]:
                return False
        return True
        
        


        