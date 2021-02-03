# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/3 11:46
# File: 0043.py
# Desc: 

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic1 = {}
        dic2 = {}
        l1 = len(num1)
        l2 = len(num2)
        for idx,num in enumerate(num1):
            k = l1-idx-1
            dic1[k] = num
        for idx,num in enumerate(num2):
            k = l2-idx-1
            dic2[k] = num
        ans = 0
        for k1, v1 in dic1.items():
            for k2, v2 in dic2.items():
                ans += int(v1) * int(v2) * 10**k1 * 10**k2
        return str(ans)