# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/21 11:16
# File: 0838.py
# Desc: 

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l = list(dominoes)
        status_c = l[0]
        status_id = 0
        for i in range(1,len(l)):
            c = l[i]
            if c == '.': continue
            elif c == 'L':
                if status_c == 'R': # 之前和当前相对，向中间靠拢
                    idl = status_id; idr = i
                    while idl < idr:
                        l[idl] = 'R'
                        l[idr] = 'L'
                        idl += 1
                        idr -= 1
                    status_id = i
                    status_c = 'L'
                else: # 当前向左，之前为空或向左，中间全向左
                    for idx in range(status_id,i): l[idx] = 'L'
                    status_id = i
            else:
                if status_c == 'R': # 之前向右，当前向右，中间全向右
                    for idx in range(status_id,i): l[idx] = 'R'
                    status_id = i
                else: # 之前向左或为空，当前向右，中间不变
                    status_c = 'R'
                    status_id = i
        if l[-1] == '.' and status_c == 'R':

