
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    # first element is defo sorted
    merge = [intervals[0]]
    
    # skip the first element
    for i in range(1,len(intervals)):
        current = intervals[i]
        last_merged = merge[-1]
         # Check if there is an overlap
        if last_merged[1] >= current[0]:
            last_merged[1] = max(current[1],last_merged[1])
        else:
           merge.append(current)
           
    return merge

intervals = [[1, 3], [2, 4], [6, 8]]

print(merge_intervals(intervals))