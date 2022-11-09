# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/09 10:49
# File: 0764.py
# Desc: 

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines = set([(i,j) for i,j in mines])
        dpzs = list()
        dpyx = list()
        for i in range(n):
            l = list()
            for j in range(n):
                l.append([0,0])
            dpzs.append(l)
            dpyx.append(l.copy())
        for i in range(n):
            for j in range(n):
                if (i,j) in mines: dpzs[i][j] = [0,0]
                else:
                    shang = dpzs[i-1][j] if i > 0 else [0,0]
                    zuo = dpzs[i][j-1] if j > 0 else [0,0]
                    dpzs[i][j] = [shang[0]+1,zuo[1]+1]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (i,j) in mines: dpyx[i][j] = [0,0]
                else:
                    xia = dpyx[i+1][j] if i < n-1 else [0,0]
                    you = dpyx[i][j+1] if j < n-1 else [0,0]
                    dpyx[i][j] = [xia[0]+1,you[1]+1]
        ret = 0
        for i in range(n):
            for j in range(n):
                z,s = dpzs[i][j]
                y,x = dpyx[i][j]
                m = min([s,x,z,y])
                ret = max(m, ret)
        return ret
