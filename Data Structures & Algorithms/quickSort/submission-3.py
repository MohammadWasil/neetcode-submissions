# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0               # first index
        e = len(pairs) - 1  # last index
        pairs = self.quick_sort_implementation(pairs, s, e)
        return pairs

    def quick_sort_implementation(self, pairs: List[Pair], s : int, e : int) -> List[Pair]:
        
        # check if the arr size is less than or equal to 1.
        if (e - s + 1) <= 1:
            return pairs

        pivot = pairs[e]
        left = s
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                # swap:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1
        
        # once done, we swap the pivot with the element n the left index.
        pairs[e] = pairs[left]
        pairs[left] = pivot

        # perform recursive step for the other psliited arrays.
        # on left, we have elemtns less than pivot, and on the rght, we have elemetns 
        # greater than or eqaul to pivot.
        pairs = self.quick_sort_implementation(pairs, s, left-1)
        pairs = self.quick_sort_implementation(pairs, left+1, e)
        return pairs