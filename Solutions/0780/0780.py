# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/4/9 11:25
# File: 0780.py
# Desc: 

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while True:
            if tx == sx and ty == sy: return True
            if sx+sy > tx and sx+sy > ty: return False
            if tx > ty:
                if tx > sum((ty,sx,sy)):
                    tx %= ty
                    if tx == 0: tx = ty
                    while tx < sx: tx += ty
                else: tx -= ty
            elif tx < ty:
                if ty > sum((tx,sx,sy)):
                    ty %= tx
                    if ty == 0: ty = tx
                    while ty < sy: ty += tx
                else: ty -= tx
            else:
                if tx != sx or ty != sy: return False
            if tx < sx or ty < sy: return False
            elif tx == 1 or ty == 1: return True
