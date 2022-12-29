# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/30 15:18
# File: 0855.py
# Desc: 


from sortedcontainers import SortedList


class ExamRoom:

    def __init__(self, n: int):
        self.sl = SortedList()  # 表示已分配的座位号（有序）
        self.n = n

    def seat(self) -> int:
        # 1. 当 sl 为空时，即还没有分配座位时，分配 0 号座位
        if not self.sl:
            self.sl.add(0)
            return 0

        # 2. 当 sl 不为空时，即已经分配了若干座位（座位号有序），那么，
        # 要么分配两端的座位（0 号座位或 n - 1 号座位），
        # 要么分配两个座位号 sl[i] 和 sl[i + 1] 之间的座位：
        #   sl[i] + (sl[i + 1] - sl[i]) // 2

        # 2.1 初始分配 idx = 0 号座位，与第一个已分配座位的距离为 diff = sl[0] - 0
        # idx: 当前分配的座位号
        # diff：记录当前分配座位号与其周围（两边）已分配座位号的最大距离
        diff, idx = self.sl[0], 0

        # 2.2 分配两个座位号 sl[i] 和 sl[i + 1] 之间的座位的情况：
        #   sl[i] + (sl[i + 1] - sl[i]) // 2
        for x, y in pairwise(self.sl):
            if (y - x) // 2 > diff:
                diff = (y - x) // 2
                idx = x + (y - x) // 2

        # 2.3 分配最后一个座位号 n - 1 的情况
        if self.n - 1 - self.sl[-1] > diff:
            diff = self.n - 1 - self.sl[-1]
            idx = self.n - 1

        self.sl.add(idx)
        return idx

    def leave(self, p: int) -> None:
        self.sl.remove(p)
