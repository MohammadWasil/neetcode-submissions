class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        word1 = abc, word2 = xyz

        res = [a x]


        """
        res = ""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]

            i += 1
            j += 1

        res += word1[i:]
        res += word2[j:]

        return res
        