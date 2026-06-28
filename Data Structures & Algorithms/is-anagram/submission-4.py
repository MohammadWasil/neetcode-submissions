class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s = "racecar", t = "carrace"

        hm = {r: +1-1-1+1=0, c:-1+1+1-1=0, a:+1-1-1+1=0, e:+1-1=0}

        """

        if len(s) != len(t):
            return False
        
        char_hashmap = defaultdict(int)

        for s_char, t_char in zip(s, t):
            char_hashmap[s_char] += 1
            char_hashmap[t_char] -= 1
        
        for char, value in char_hashmap.items():
            if char_hashmap[char] != 0:
                return False
        return True
        
