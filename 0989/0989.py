# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/22 12:43
# File: 0989.py
# Desc: 
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return [int(i) for i in str(int("".join([str(j) for j in A])) + K)] if K else A
