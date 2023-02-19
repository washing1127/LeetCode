# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/19 10:47
# File: 1792.py
# Desc: 


class Entry:
    __slots__ = 'p', 't'

    def __init__(self, p: int, t: int):
        self.p = p
        self.t = t

    def __lt__(self, b: 'Entry') -> bool:
        return (self.t - self.p) * b.t * (b.t + 1) > (b.t - b.p) * self.t * (self.t + 1)

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [Entry(*c) for c in classes]
        heapify(h)
        for _ in range(extraStudents):
            heapreplace(h, Entry(h[0].p + 1, h[0].t + 1))
        return sum(e.p / e.t for e in h) / len(h)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/maximum-average-pass-ratio/solutions/2118606/zui-da-ping-jun-tong-guo-lu-by-leetcode-dm7y3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
