class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        s = "Was it a car or a cat I saw?"
        s = wasitacaroracatisaw
            i                 j
             i               j
              i             j
               i           j
                i         j
                 i       j
                  i     j
                   i   j
                    i j
                     i=j
        Stop whe i ==j
        also need to check for alphanum character for every character at i and j
        """
        i = 0
        j = len(s) - 1


        while i < j:

            # moves the index if char on l is not alpha numeric.
            while i < j and not s[i].isalnum():
                i += 1
            # moves the index if char on r is not alpha numeric.
            while i < j and not s[j].isalnum():
                j -= 1
            
            # if they both are alphanumeric
            if s[i].lower() != s[j].lower():
                return False
            
            # udpate the l and r pointer as usual
            i += 1
            j -= 1
        
        return True