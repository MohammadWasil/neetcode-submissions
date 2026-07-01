class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1, 2, 2, 3, 3, 3] ->k = 2, res = [2, 3]
        hashmap = {1: 1, 2:1+1, 3:1+1+1} -> select the k key with the maximum value
        hashmap = {1:1, 2:2, 3:3}
        """

        hashmap = defaultdict(int)

        for i in nums:
            hashmap[i] += 1
        
        hashlist = [(k, v) for k, v in hashmap.items()]

        sorted_dict = sorted(hashlist, key=lambda element: element[1], reverse=True)
        
        result = []
        for sort_pair in sorted_dict:
            result.append(sort_pair[0])
            
        return result[:k]



        