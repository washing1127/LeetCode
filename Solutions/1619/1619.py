# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/14 10:09
# File: 1619.py
# Desc: 


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        return sum(sorted(arr)[len(arr) // 20:-(len(arr) // 20)]) / (len(arr) // 20) / 18
