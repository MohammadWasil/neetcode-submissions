class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        s = "Hello World"
        Strip all the empty white spaces on the right
        split the string based on the empty space, and put it into list
        take the last elemene tomfr the list
        count the len of the last element
        """

        #return len(s.rstrip().split()[-1])

        """
        let length be the length of the last element
        s = "Hello World "
        0               i -> white space, ignore it and i--
        1              i -> not a white space, length += 1 => 1, i--
        2             i  -> not a white space, length += 2 => 2, i-- 
        3            i  -> not a white space, length += 3 => 2, i-- 
        4           i  -> not a white space, length += 4 => 2, i-- 
        5          i  -> not a white space, length += 5 => 2, i-- 
        6         i  -> white space, ignore it and i--

        s = "a"
        0    i

        O(N) TC and O(1) SC
        """
        length = 0
        i = len(s) - 1 # pointing to the last element

        while s[i] == " ":
            i -= 1
        
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
