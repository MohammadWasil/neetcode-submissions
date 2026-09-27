class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        """

        res = []

        for num in nums1:
            res.append(nums2.index(num))
        
        return res
        