class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        logs = ["d1/","d2/","../","d21/","./"]

        -> d1/
            -> d2 
                -> inside d2 (followed by ../)
            -. d21/
                -> currently here    
        => d1/d21/. > therefore, we need to perform 2 ../ operations.
        Lets use stack, last in first out.

        1. Keep on adding element sn stack until we received "../" operation: 
            stack = [d1/, d2/]
        2. "../" -> pop the last element from the stack.
            stack = [d1/,]
        3. continue with next operations:
            stack = [d1/, d21/], 
        4. stop the program when "./"
        5. return the length of the stack as the minimum number of operations.
        """
        stack = []

        for log in logs:
            if log not in ["./", "../"]:
                stack.append(log)
            if log == "../" and len(stack) > 0:
                stack.pop()
        return len(stack)
