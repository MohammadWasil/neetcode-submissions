class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={} # val: index + 1

        for i, n in enumerate(numbers):
            i+=1
            a = target - n
            if a in hashmap:
                if hashmap[a] < i:
                    return [hashmap[a], i]
            hashmap[n] = i
        return []