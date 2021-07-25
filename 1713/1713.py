# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/26 10:42
# File: 1713.py
# Desc: 


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        idx_dict = {num: i for i, num in enumerate(target)}
        stack=[]
        for num in arr:
            if num in idx_dict:
                idx=idx_dict[num]
                i= bisect.bisect_left(stack,idx)
                if len(stack)==i:
                    stack.append(0)
                stack[i]=idx
        return len(target)-len(stack)