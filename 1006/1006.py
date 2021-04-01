# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/1 10:43
# File: 1006.py
# Desc: 

class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1: return 1;
        if N == 2: return 2;
        if N == 3: return 6;
        if N == 4: return 7;
        if N % 4 == 0: return N+1;
        if N % 4 <= 2: return N+2;
        else: return N-1;

        # ans = 0
        # positive = True
        # for i in range(N,0,-4):
        #     tempb = 0
        #     if i >= 4: 
        #         tempa = i * (i-1) // (i-2)
        #         tempb = i-3
        #     elif i == 3: 
        #         tempa = i * (i-1) // (i-2)
        #     elif i == 2: 
        #         tempa = i * (i-1)
        #     elif i == 1: 
        #         tempa = i

        #     if positive: 
        #         ans += tempa + tempb
        #         positive = False
        #     else:
        #         ans -= tempa
        #         ans += tempb

        # return ans