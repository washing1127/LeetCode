# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/30 11:52
# File: 0190.py
# Desc: 
class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        s = bin(n)[2:]
        s = "0"*(32-len(s))+s
        for idx, i in enumerate(s):
            num += 2**idx*int(i)
        return num

        # DateTime: 2021/3/29 16:55

        # ans = 0
        # for i in range(32):
        #     res = n % 2
        #     ans = (ans << 1) + res
        #     n >>= 1
        # return ans

        # return int(f"{int(bin(n)[2:]):032d}"[::-1],2)