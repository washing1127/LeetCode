# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/31 9:15
# File: 2037.py
# Desc: 

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ret = 0
        for i, j in zip(seats, students):
            ret += abs(j-i)
        return ret
