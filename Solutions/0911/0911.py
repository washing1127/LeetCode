# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/11 10:29
# File: 0911.py
# Desc: 

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        tops = []
        voteCounts = defaultdict(int)
        voteCounts[-1] = -1
        top = -1
        for p in persons:
            voteCounts[p] += 1
            if voteCounts[p] >= voteCounts[top]:
                top = p
            tops.append(top)
        self.tops = tops
        self.times = times
        
    def q(self, t: int) -> int:
        l, r = 0, len(self.times) - 1
        # 找到满足 times[l] <= t 的最大的 l
        while l < r:
            m = l + (r - l + 1) // 2
            if self.times[m] <= t:
                l = m
            else:
                r = m - 1
        # 也可以使用内置的二分查找的包来确定 l
        # l = bisect.bisect(self.times, t) - 1
        return self.tops[l]


