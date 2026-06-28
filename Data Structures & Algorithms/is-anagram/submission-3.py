class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first lets create a hashmap of the first inout string, s
        string_hashmap = {}
        #for char in s:
        #    if char in string_hashmap:
        #        string_hashmap[char] += 1
        #    else:
        #        string_hashmap[char] = 1
        
        #for char in t:
        #    if char in string_hashmap:
        #        string_hashmap[char] -= 1
        #    else:
        #        string_hashmap[char] = 1

        if len(s) != len(t):
            return False
        for char1, char2 in zip(s, t):
            if char1 not in string_hashmap:
                string_hashmap[char1] = 0
            if char1 != char2 and char2 not in string_hashmap:
                string_hashmap[char2] = 0
            
            if char1 in string_hashmap:
                string_hashmap[char1] += 1
            if char2 in string_hashmap:
                string_hashmap[char2] -= 1


        return True if all(counter==0 for _, counter in string_hashmap.items()) else False