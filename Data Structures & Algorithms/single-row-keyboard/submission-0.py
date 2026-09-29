class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """
        """
        total_time = 0
        current_index = 0
        for char in word:
            next_word_index = keyboard.index(char)
            total_time += abs(next_word_index - current_index)
            current_index = next_word_index
        
        return total_time
        