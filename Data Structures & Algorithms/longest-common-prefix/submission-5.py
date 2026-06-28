class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        hashmap = {}
        min_size_word = len(min(strs, key=len)) # get the length of the shortest word # 3

        for string in strs:
            for char in range(min_size_word + 1): # 1
                if string[:char] in hashmap:
                    hashmap[string[:char]] += 1
                else:
                    hashmap[string[:char]] = 1

        # get the key with the maximum value/counter
        possible_prefix = []
        longest_key = ""
        for prefix, counter in hashmap.items():
            if counter == len(strs) and len(prefix) > len(longest_key):
                longest_key = prefix
        #return max(possible_prefix, key=len) if len(possible_prefix) >0 else ""
        return longest_key


