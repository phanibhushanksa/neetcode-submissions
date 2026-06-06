class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])


        result = [intervals[0]]



        for i in range(1,len(intervals)):
            current = intervals[i]

            # compare with last element in the result
            last = result[-1]
            

            # check for overlap

            if last[1]>=current[0]:
                last[1] = max(last[1], current[1])

            else:
                result.append(current) 


        return result
