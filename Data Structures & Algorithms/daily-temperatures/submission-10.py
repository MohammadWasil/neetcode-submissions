class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """res = []
        n = len(temperatures)

        for i in range(n):
            j = i + 1
            count = 1
            while j < n : #and temperatures[i] >= temperatures[j]:    
                #if j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    #res[i] = j - i
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            res.append(count)
        return res"""
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res


        