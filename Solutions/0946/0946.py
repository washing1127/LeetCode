# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/08/31 11:11
# File: 0946.py
# Desc: 


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        temp = []
        while popped:
            if temp and temp[-1] == popped[0]:
                temp.pop()
                popped.pop(0)
            elif pushed:
                temp.append(pushed.pop(0))
            else: break
        return temp == popped and len(temp) <= 1
