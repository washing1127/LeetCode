# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/19 19:23
# File: 1450.py
# Desc: 


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return len([i for i,j in zip(startTime, endTime) if i <= queryTime and j >= queryTime])
