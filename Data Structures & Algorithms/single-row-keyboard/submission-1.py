class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """
        set current_index = 0, our initial point.
        iterate the word array
        take the frst word, get the index (word_index) of that word from the keyboard list
        substract the word_index from current_index, abolute value, and add to the tiak time taken
        """
        total_time = 0
        current_index = 0
        for char in word:
            next_word_index = keyboard.index(char)
            total_time += abs(next_word_index - current_index)
            current_index = next_word_index
        
        return total_time
        