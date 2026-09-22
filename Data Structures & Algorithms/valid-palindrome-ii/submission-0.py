class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
              a b b d a
        0->   l       r -> l=r, l+1, r-=1
        1->     l   r -> l != r, remove one of them one by one.
                                 1. a _ b d a -> skip l
                                        l r    -> check for palindrome
                                 2. a b b _ a -> skip r
                                      l r     -> check for palindrome
                                 One of them should be true
        """

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # skips l and r one by one
                skip_l = s[l+1:r+1] # r+1 because last index is not included, therefore, +1
                skip_r = s[l:r] # skipping last element r here, and using the l
                # compare the remaining part with their palindrome/reverse string
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            l += 1
            r -= 1
        return True
        