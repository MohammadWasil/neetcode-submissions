class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix_hashmap = {}
        # b : [0, 1, 2, 3]
        # ba: [0, 1, 2, 3]
        # bat: [0, ]
        # bag: [1,]
        # ban: [2, 3]

        # filter out the one which have less than the number of elements in strs.
        # get the string wth the longest length

        # shortest word from the list
        #length_word = 201
        #for word in strs:
        #    if len(word) < length_word:
        #        length_word = len(word)
        length_word = min(len(w) for w in strs)

        # create hashmap
        word_set = []
        for w in range(1, length_word + 1): # 3
            for i, character in enumerate(strs):

                # get the value
                stored_list = []
                if character[:w] in prefix_hashmap:
                    stored_list = prefix_hashmap[ character[:w] ]
                stored_list.append(i)
                prefix_hashmap[character[:w]] = stored_list

        possible_words = []
        for k, v in prefix_hashmap.items():
            if len(v) == len(strs):
                possible_words.append(k) # ["b", "ba"]

        if possible_words:
            final_string = max(possible_words, key=len)
            return final_string       
        return ""
