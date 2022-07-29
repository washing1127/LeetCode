# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/29 15:40
# File: 0593.py
# Desc: 


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2: return False
        p1,p2,p3,p4 = sorted([p1,p2,p3,p4], key=lambda x: (x[0], x[1]))
        if p4[0] - p2[0] == p3[0] - p1[0] and p4[1] - p2[1] == p3[1] - p1[1]: #平行四边形
            x1 = p4[0] - p2[0]
            x2 = p1[0] - p2[0]
            y1 = p4[1] - p2[1]
            y2 = p1[1] - p2[1]
            if x1*x2 + y1*y2 == 0: #矩形
                x1 = p4[0] - p1[0]
                x2 = p3[0] - p2[0]
                y1 = p4[1] - p1[1]
                y2 = p3[1] - p2[1]
                if x1*x2 + y1*y2 == 0: #对角线垂直
                    return True
        return False
