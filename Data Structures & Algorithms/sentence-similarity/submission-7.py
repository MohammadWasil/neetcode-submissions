class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        """
        1. Compare the string length, if they are not equal, return False. Else, continue
        2. create a hashset, of all the possible words in pairs, for all possible combinations:
           {
            great: [fine], 
            acting: [drama], 
            skills: [talent], 
            fine:[great], 
            drama: [acting], 
            talent: [skills]
            }
        3. if ith word in both sentence are the same, contoinue
        4. if word ins sentence2 is in hashset, with keys coming from ith word of sentence1, continue
            sentence2 <-> hashset[sentence1]
            i=0 -> fine <-> hashset[great] = fine <- both are the same
            i=1 -> drama <-> hashset[acting] = drama <- both are the same
            i=2 -> talent <-> hashset[skills] = talent <- both are the same
            Return True
        """

        if len(sentence1) != len(sentence2):
            return False
        
        wordToSimilarWords = defaultdict(set)
       
        for word1, word2 in similarPairs:
            wordToSimilarWords[word1].add(word2)
            wordToSimilarWords[word2].add(word1)

        for i in range(len(sentence1)):
            
            if sentence1[i] == sentence2[i] or sentence2[i] in wordToSimilarWords[sentence1[i]]:
                continue
            return False
        return True
        