class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1, 2, 2, 3, 3, 3], k=2
        # answer: [2, 3]
        # [1, 2], k=2
        # [1, 2]
        
        #hashmap = {}
        #unique_frequent_element = []
        #for i in nums:
        #    if i not in unique_frequent_element:
        #        if i not in hashmap:
        #            hashmap[i] = 0
        #        hashmap[i] += 1#

        #        if hashmap[i] >= k:
        #            unique_frequent_element.append(i)
        #return unique_frequent_element

        counter = [0] * (len(nums)+1)
        
        # cate a hashmap
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1

        arr=[]
        for num, count in hashmap.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res







            