class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        s = n e e t
            i     j , swap t with n
              i j     swap e with e
              if i > j -> stop
        """

        temp = None
        i = 0
        j = len(s) - 1
        while j > i:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1


        
        