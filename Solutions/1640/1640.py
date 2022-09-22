# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/22 15:38
# File: 1640.py
# Desc: 


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        while arr:
            for i in pieces:
                if i[0] == arr[0]:
                    if not i == arr[:len(i)]: return False
                    arr = arr[len(i):]
                    break
            else: return False
        return True
