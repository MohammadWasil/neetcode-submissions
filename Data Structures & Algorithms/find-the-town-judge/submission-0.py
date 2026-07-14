class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        [[1,3],[4,3],[2,3]]
        1 -> 3
        4 -> 3
        2 -> 3 ==? therefore, 3 is the judge.
        indegree = {1:0, 2:0, 3:0, 4:0}
        outdegree = {1:0, 2:0, 3:0, 4:0}

        outdegree[src] => outdegree[1] += 1
         outdegree = {1:1, 2:1, 3:0, 4:1}
         indegree = {1:0, 2:0, 3:3, 4:0}

         Chck, whichever key from outgoing is 0, and the same key has n-1 (everybody loves the judge)

        """
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for src, dst in trust:
            outdegree[src] += 1
            indegree[dst] += 1
        
        for i in range(1, n+1):
            if outdegree[i] == 0 and indegree[i] == n-1:
                return i
        return -1
        