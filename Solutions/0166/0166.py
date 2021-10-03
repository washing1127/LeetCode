# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/3 17:38
# File: 0166.py
# Desc: 

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        fs = ""
        if numerator * denominator < 0: fs = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)

        zs = str(numerator // denominator)
        ys = numerator % denominator
        if not ys: return fs + zs
        ans = zs + "."
        dic = dict()
        idx = len(ans)
        dic[ys] = idx
        while ys:
            idx += 1
            ys *= 10
            zs = ys // denominator
            ans += str(zs)
            ys = ys % denominator
            if ys in dic.keys():
                i = dic[ys]
                ans = ans[:i] + "(" + ans[i:] + ")"
                return fs + ans
            elif ys != 0:
                dic[ys] = idx
        return fs + ans
