"""
给出一个区间的集合，请合并所有重叠的区间。
"""
def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][-1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][-1] = max(merged[-1][-1], interval[-1])
    return merged