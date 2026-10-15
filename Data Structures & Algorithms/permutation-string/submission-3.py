class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s2 = "l e c a b e e"
              i   j

              i=0   j=2 -> l in s1 -> F -> i=1,j=3
                i   j   -> e in s1 -> F -> i=2,j=4
                  i   j -> c in s1 -> T -> i=3,j=4
                    i j -> a in s1 -> T -> i=4,j=4
                      i/j->b in s1 -> T -> i=5,j=4



        """
        """window = len(s1)
        i = 0
        j = window - 1
        words = list(s1)
        
        while j < len(s2):
            
            if s2[i] not in words:
                # update the window here
                j += 1
            else:
                words.remove(s2[i])
            i += 1

            if i == j:
                return True
        return False
        """
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False