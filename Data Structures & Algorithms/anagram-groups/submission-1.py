class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        idea: word_dict = 
        {
        [1, 0, 1, 0, 0, ...., 0, 1, 0, 0, 0, 0, 0, 0] : ["act", "cat"], 
         a  b  c  d  e        s  t  u  v  w  x  y  z 
         ....
        }
        ["act","pots","tops","cat","stop","hat"]

        "act"
        1. set the value of the index where the alphabet lies in the list of 0's.
        count = [1, 0, 1, ....]

        2. add to th dict, with values the word itself.
        dict[ (1, 0, 1, ....)  ] : ["act"]

        "pots"
        count = [0, 0, 0, ....., 1, ..1, ...0..., 1]
        dict[ (0, 0, 0, ....., 1, ..1, ...0..., 1)  ] : ["pots"]

        and so on...

        Finally, return the vaues of the dict, and convert them to list.
        """
        word_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1
            word_dict[tuple(count)].append(word)
        
        return list(word_dict.values())