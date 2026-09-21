class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        s = "code"

        return score

        0 -> c - o -> add it to score -> 99-111 = 12 = score
        1 -> o - d -> add it to score -> 111-100 = 11 -> score = 12 + 11 = 23
        2 -> d - e -> add it to score -> 100-101 = 1 -> score = 23 + 1 = 24
        """
        score = 0

        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i+1]))
        
        return score


        