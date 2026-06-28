class Solution:
    def isValid(self, s: str) -> bool:

        # check of the len is odd or even -> odd return False
        # create a hashmap with key as brackers
        # and we can assign some complimentary values (-1/+1)
        # We can two pointers, left and right
        # and check if the value of the brackets from hashmap sums to 0.
        # and if they dont, return False, or else continue the loop
        # ()[]{}

        """hashmap = {
            "(" : -1,
            ")" : +1,
            "[" : -2,
            "]" : +2,
            "{" : -3,
            "}" : +3,
        }

        left = 0
        right = len(s) - 1

        while left <= right:
            if hashmap[s[left]] + hashmap[s[right]] != 0:
                return False
            left += 1
            right -= 1
        
        return True"""

        stack = []
        hashmap = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }

        for char in s:
            # if closing bracket is detcted.
            # this means the previous element should be an opeing bracker of the same shape
            # of it, remove it forom the stack
            if char in hashmap.keys():
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if len(stack) == 0 else False
