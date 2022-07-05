# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/05 10:15
# File: 0729.py
# Desc: 


class MyCalendar:

    def __init__(self):
        self.l = []


    def book(self, start: int, end: int) -> bool:
        for a,b in self.l:
            if start <= a < end or start < b <= end or a <= start and b >= end:
                return False
        self.l.append([start, end])
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
