class Solution:
    def isHappy(self, n: int) -> bool:
        """

        n = 19
        19 -> 82 -> 68 -> 100 -> 1

        # at every node, we need to calcuate the happy number
        # slow and fast pointer to detrmin if there is a cycle in the linkedlist

        """

        def get_happy_number(n):
            sum_ = 0

            while n>0:
                sum_ += (n % 10) ** 2 # 9**2=81
                n //= 10          # 1**2=1

            return sum_
        
        slow = get_happy_number(n)
        fast = get_happy_number(get_happy_number(n))

        while fast != 1:
            slow = get_happy_number(slow)
            fast = get_happy_number(get_happy_number(fast))

            if slow == fast:
                return False
        
        return fast == 1