class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operator = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(b-a)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(float(b) / a))

        return stack[0]