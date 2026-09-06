class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        here s1 char frequency is created using a list
        the index of the list corresponds to lower case alphabets- 1 to 26
        ord() is used to display the ascii equivalent of the char

        """
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        if len(s1) > len(s2):
            return False
        for right in range(len(s1)):
            s1_freq[ord(s1[right]) - ord('a')] += 1
            s2_freq[ord(s2[right]) - ord('a')] += 1
        if s1_freq== s2_freq:
            return True

        for right in range(len(s1),len(s2)):
            s2_freq[ord(s2[right]) - ord('a')] += 1
            s2_freq[ord(s2[right-len(s1)]) - ord('a')] -= 1
            if s1_freq == s2_freq:
                return True
        return False



        