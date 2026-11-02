class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        procsss the task that has the highest frequency
        tasks = ["A","A","A","B","C"], n = 3
        Process A first, and then B and then C, all A should have atleast time=3.
        
        1. Create frequncy of tasks:
        {A:3, B:1, C:1}
        2. heapify all the values from the frequency dict
                -3
            -1      -1
        3. pop the first element from heap, and add 1 to it, only if the heap is nonempty
            -3 + 1 = -2
            time=1
            - Add the -2 along with the time + n tot he queue
            Queue = ([-2, time+n]) = ([-2, 4]), so this task needs to wait 4 unit
        4. If it is empty, take the time from the queue
        5. comapre the time from the queue with the current time, if they are equal, then 
        pop the elemtm from the queue, and push it to heap

        """

        freq = Counter(tasks)
        heap = [-f for f in freq.values()]
        heapq.heapify(heap)

        time = 0
        queue = deque()

        while heap or queue:
            time += 1
            if not heap:
                # get the time from the queue
                time = queue[0][1]
            else:
                first_value = 1 + heapq.heappop(heap)
                if first_value:
                    queue.append((first_value, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time


        