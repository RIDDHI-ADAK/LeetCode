class Solution:
    def insert(self, intervals, newInterval):

        result = []
        i = 0
        n = len(intervals)

        newStart = newInterval[0]
        newEnd = newInterval[1]

        # 1. Add intervals completely before newInterval
        while i < n and intervals[i][1] < newStart:
            result.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < n and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1

        # 3. Add merged newInterval
        result.append([newStart, newEnd])

        # 4. Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result