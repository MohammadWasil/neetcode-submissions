class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #TODO:
        l = 0
        hashset = set()
        longest_substring = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            longest_substring = max(r-l+1, longest_substring)
        return longest_substring
        
        
        
        
        














        
        
        #l = 0
        #hashset = set()
        #max_length = 0

        #for r in range(len(s)):
            
        #    while s[r] in hashset:
        #        hashset.remove(s[l])
        #        l += 1

        #    hashset.add(s[r])
        #    max_length = max(r-l+1, max_length)
        #return max_length

 