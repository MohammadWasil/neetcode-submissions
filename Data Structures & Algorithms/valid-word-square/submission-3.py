class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        """
        ["abcd",
         "bnrt",
         "crmy",
         "dtye"]
        
        words[:][0] <-> word[0]
        "ball",
        "area",
        "read",
        "lady"
        1. Ignore the diagonal elements
        2. take the frst row and first colume, except the value at index [i,i],
        and compare the values.
        00, 01, 02, 03
        10, 11, 12, 13
        20, 21, 22, 23
        30, 31, 32, 33
        3. If anytime the values in i-j vs j-i are different, return False.
        4. Next, move to smaller squre, ignore the diag values, and compare the off diagonal values jst as before. 

        Edge Case: we can comparison operative before looping to avoud Out of Index error.

        "ball",
        "asee",
        "let",
        "lep"
        """
        for i in range(len(words)): # first word - ball
            for j in range(len(words[i])): # col word - barl
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]: # dont want to compare the diagonal values.
                    return False    
        return True