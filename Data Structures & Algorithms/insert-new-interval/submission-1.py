class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        st = []
        st.append(intervals[0])
        
        for i in range(1,len(intervals)):
            curr = intervals[i]
            last = st[-1]

            if last[1] >= curr[0]:
                last[0] = min(last[0],curr[0])
                last[1] = max(last[1],curr[1])
            else:
                st.append(curr)
        
        return st
            



        