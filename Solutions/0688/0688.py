# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/17 17:18
# File: 0688.py
# Desc: 
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def p(pos) -> tuple[list]:
            a, b = pos
            a1 = a2 = a-2
            a3 = a4 = a-1
            a5 = a6 = a+1
            a7 = a8 = a+2
            b1 = b7 = b-1
            b2 = b8 = b+1
            b3 = b5 = b-2
            b4 = b6 = b+2
            li = []
            if a1 >= 0 and b1 >= 0: li.append((a1,b1))
            if a2 >= 0 and b2 < n: li.append((a2,b2))
            if a3 >= 0 and b3 >= 0: li.append((a3,b3))
            if a4 >= 0 and b4 < n: li.append((a4,b4))
            if a5 < n and b5 >= 0: li.append((a5,b5))
            if a6 < n and b6 < n: li.append((a6,b6))
            if a7 < n and b7 >= 0: li.append((a7,b7))
            if a8 < n and b8 < n: li.append((a8,b8))
            return li
        pos_list = {(row, column):1}
        ret = 1
        for i in range(k):
            new_pos = dict()
            num1 = 0
            num2 = 0
            for pos, v in pos_list.items():
                not_out_list = p(pos)
                num1 += len(not_out_list)*v
                num2 += 8*v
                for po in not_out_list:
                    if po not in new_pos: new_pos[po] = v
                    else: new_pos[po] += v
            if not num2 or not num1: return 0
            ret *= num1/num2
            pos_list = new_pos
        return ret
