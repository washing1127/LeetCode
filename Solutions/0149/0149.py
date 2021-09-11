# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/24 11:07
# File: 0149.py
# Desc: 

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def checkLine(p1, p2, p3):
            if p3[1] == p2[1] == p1[1] or p1[0] == p2[0] == p3[0]: return True
            elif p3[1] != p2[1] and p3[1] != p1[1]:
                k1 = (p3[0] - p2[0]) / (p3[1] - p2[1])
                k2 = (p3[0] - p1[0]) / (p3[1] - p1[1])
                return f"{k1:.8f}" == f"{k2:.8f}"
            else: return False

        if len(points) < 3: return len(points)
        max_num = 2
        for i in range(len(points)):
            p1 = points[i]
            for j in range(i+1, len(points)):
                num = 2
                p2 = points[j]
                for k in range(j+1, len(points)):
                    p3 = points[k]
                    if checkLine(p1,p2,p3):
                        num += 1
                        print(p1,p2,p3)
                max_num = max(max_num, num)

        return max_num
