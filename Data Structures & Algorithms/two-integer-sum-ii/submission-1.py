class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #hashmap={} # val: index + 1

        #for i, n in enumerate(numbers):
        #    i+=1
        #    a = target - n
        #    if a in hashmap:
        #        if hashmap[a] < i:
        #            return [hashmap[a], i]
        #    hashmap[n] = i
        #return []

        # two pointer solution:
        l = 0
        r = len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum < target: # this means we curernt val is reall smaller thsn the target
            # we need to use some bigegr number, logically make sense to push l to the right
                l += 1
            elif current_sum > target:
                # logically make sense to move r to the left
                r -= 1

            if current_sum == target:
                return [l+1, r+1]
        return []

