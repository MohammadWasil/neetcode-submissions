class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        blocks = "WBBWWBBWBW", k = 7

        Init:
        Lets create a sliding window of size 7
        count the number of W's in the window, prev = num(W)

        iterate:
        remove the first element from the sliding window -> if W, W-= 1
        add the next element next to th sliding window -> if W, W+= 1
        update prev = min(prev, num(W))
        Until reaches the end of the str array.

        
        window = [W, B, B, W, W, B, B], w_count = 3, prev = 3 -> init.

        Loop 1:
        0123456789
        WBBWWBBWBW
               |
        window [x, B, B, W, W, B, B, W] w_count = 3-1+1=3, prev=min(3, 3)=3

        Loop 2:
        0123456789
        WBBWWBBWBW
                |
        window [x, B, W, W, B, B, W, B] w_count = 3, prev=3

        Loop 3:
        0123456789
        WBBWWBBWBW
                 |
        window [x, W, W, B, B, W, B, W] w_count = 3+1=4, prev=min(3, 4) = 3
        """

        window = []

        w_count = 0
        prev = 0
        for i in range(k):
            window.append(blocks[i])
            if blocks[i] == "W":
                w_count += 1
        prev = w_count
        # slide the window.
        for i in range(k, len(blocks)):

            # remove the first element from the window.
            block_value = window.pop(0)

            # Add the new element to the end of the window
            window.append(blocks[i])

            if block_value == "W":
                w_count -= 1
            if blocks[i] == "W":
                w_count += 1
            prev = min(prev, w_count)

        return prev








        