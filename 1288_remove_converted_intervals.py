def removeCoveredIntervals(intervals: list) -> int:
    if len(intervals) == 1:
        return 0
    
    # Check [a,b] against [c,d] c <= a & b <= d
