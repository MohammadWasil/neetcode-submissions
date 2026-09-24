class Solution:
    def confusingNumber(self, n: int) -> bool:
        """
        1. reverse the numbers
        2. iterate each number thorugh the defined hashmap, and replace the original values
        with the values in the hashmaps.
        4. If the keys not present in hashmap, return False.
        5. If the resultant new num after the reverse and mapping is same s origibal, return Fakse
        6. Else return True
        """
        original_num = n
        hashmap = {0:0, 1:1, 6:9, 8:8, 9:6}

        # reverse the number.
        reverse = 0

        # n=1234
        while n != 0: # stops when n = 0.
            last_digit = n % 10 # 4 -> 3 -> 2 -> 1

            # if the last_digit is not in hashmap, no need to go thoruhg the whole loop
            # Just return False
            if last_digit not in hashmap.keys():
                return False

            reverse = reverse * 10 + hashmap[last_digit] # 4 -> 43 -> 432 -> 4321
            n = n // 10 # 123 -> 12 -> 1 -> 0

        return reverse != original_num


        