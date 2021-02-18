# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/18 17:39
# File: 0995.py
# Desc: 

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:

        n = len(A)
        diff = [0] * (n+1)
        ans = 0
        revCnt = 0

        for i in range(n):
            revCnt += diff[i]
            if (A[i]+revCnt) % 2 == 0:
                if i + K > n: return -1
                ans += 1
                revCnt += 1
                diff[i+K] -= 1
        return ans
