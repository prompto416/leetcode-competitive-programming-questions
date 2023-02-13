def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    
    intervals.sort(key=lambda x:x[1])
    print(intervals)
    output = 0 
    max_end = float('-inf')
    for start,end in intervals:
        if start >= max_end:
            print(start,end,max_end)
            max_end = end
        else:
            output += 1
    return output
            

intervals = [[1,2],[2,3],[3,4],[1,3]]

eraseOverlapIntervals(intervals)

