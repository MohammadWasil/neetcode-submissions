class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l = 0 # word
        r = 0 # abbr

        while l < len(word) and r < len(abbr):
            if abbr[r].isnumeric():

                # edge case: when number leads with 0
                if abbr[r] == "0":
                    return False

                # process multi digit numbers
                num = 0
                while r < len(abbr) and abbr[r].isdigit():
                    num = num * 10 + int(abbr[r])
                    r += 1

                # if num is found in abbr, increament l by the num in abbr
                l += num

            else:
                # compare the values one by one, to check for inconsistent shortforms.
                if word[l] != abbr[r]:
                    return False
                l += 1
                r += 1
        
        return l == len(word) and r == len(abbr)
