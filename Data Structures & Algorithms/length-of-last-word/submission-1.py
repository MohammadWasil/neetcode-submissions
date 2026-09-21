class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        s = "Hello World"
        Strip all the empty white spaces on the right
        split the string based on the empty space, and put it into list
        take the last elemene tomfr the list
        count the len of the last element
        """

        return len(s.rstrip().split()[-1])