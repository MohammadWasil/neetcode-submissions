class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [[1,3],[1,5],[6,7]]

        sort the intervals based on their first value
        output = [add the first element]

        Go through the element except the first one
        compare the curr start witht he last end time.
        if it is smaller, than update the end tme by taking max of boht of the end times
        else,just keep on appending the intervals
        """

        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start_time, end_time in intervals:
            prev_end_time = output[-1][1]
            if start_time <= prev_end_time:
                # merge the intervals
                output[-1][1] = max(end_time, prev_end_time)
            else:
                output.append([start_time, end_time])

        return output
