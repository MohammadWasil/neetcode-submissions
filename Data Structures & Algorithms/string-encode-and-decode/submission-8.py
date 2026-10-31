class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encoding the string by storing a length, a delim "#" and the word itself
        in a long string.
        ["Hello","World"]
        Encoded: "5#Hello5#World"
        """
        res = []

        for words in strs:
            res.append(str(len(words)))
            res.append("#")
            res.append(words)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """
        To decode "5#Hello5#World" bck to ["Hello","World"]

        5 # H e l l o 5 # W o r l d
        i
          j
        len = 5 [i:j]
            i         j
        move i to j   i=j  

        1. Find the length of the first word
            - keep on increaing the j, until we find the #
            - i:j -> corresponds to the length of the word
        2. move the i to the element next to # -> i = j+1
        3. move the j to the end of the current word, -> j = legth + i
        4. regenerate the word -> word=s[i:j]
        5. update the i, to start with the next word: i=j
        """
        res = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            word = s[i:j]
            res.append(word)
            i = j
        return res

