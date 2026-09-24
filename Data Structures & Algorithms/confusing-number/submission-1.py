class Solution:
    def confusingNumber(self, n: int) -> bool:
        """
        """
        original_num = n
        hashmap = {"0":0, "1":1, "6":9, "8":8, "9":6}

        # reverse the number.
        reverse = 0

        # n=1234
        while n != 0: # stops when n = 0.
            last_digit = n % 10 # 4 -> 3 -> 2 -> 1
            reverse = reverse * 10 + last_digit # 4 -> 43 -> 432 -> 4321
            n = n // 10 # 123 -> 12 -> 1 -> 0
        
        new_num = ""
        for num in str(reverse):
            if num not in hashmap.keys():
                return False
            new_num += str(hashmap[num])

        if int(new_num) == original_num:
            return False
        return True


        