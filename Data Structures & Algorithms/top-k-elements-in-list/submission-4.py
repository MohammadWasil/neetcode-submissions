import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1, 2, 2, 3, 3, 3] ->k = 2, res = [2, 3]
        hashmap = {1: 1, 2:1+1, 3:1+1+1} -> select the k key with the maximum value
        hashmap = {1:1, 2:2, 3:3}
        """

        # Create hashmaps
        #hashmap = defaultdict(int)

        # populate them
        #for i in nums:
        #    hashmap[i] += 1
        
        # better to convertthem into list of tuples
        #hashlist = [(k, v) for k, v in hashmap.items()]

        # sort them based on the second value of the tuple
        #sorted_list = sorted(hashlist, key=lambda element: element[1], reverse=True)
        
        #return [pair[0] for pair in sorted_list[:k]]

        hashmap = defaultdict(int)

        # populate them
        for i in nums:
            hashmap[i] += 1

        heap = []
        for key, value in hashmap.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # <- get the key 
        
        return res






        