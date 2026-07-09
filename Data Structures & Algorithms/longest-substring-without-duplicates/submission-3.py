class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        dynamic window:
        -> z x y z x y z
           lr           -> loop thru window to check if r in window or not, if yes, remove the element l untik satisfied. add z, [z]
           l r          -> add x, [zx]
           l   r        -> add y, [zxy]
           l     r      -> remove the left most z, and add the new z -> [xyz], ncrement l
             l     r    -> remove x and add right x, increment l, [yzx]
               l     r  -> remove left y, and new y, [zxy]
                 l     r-> remove left z and new z, [xyz]

        r is at the end, stop.
        return the len of the dynamic window
        """

        l = 0
        window = []
        res = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.append(s[r])
            r += 1
            res = max(res, len(window))

        return res
