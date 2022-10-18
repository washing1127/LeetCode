# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/18 11:16
# File: 0902.py
# Desc: 


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = [int(i) for i in digits]
        length = len(digits)
        weishu = 0
        temp = n
        while temp:
            weishu += 1
            temp //= 10

        ret = 0
        for i in range(1, weishu):
            ret += length ** i
        # ¡ü¡ü¡ü¡ü¡ü¡ü¡ü¡ü¡ü the lenght of new number < n
        # print(ret)
        l = [int(i) for i in str(n)]
        dp = []
        for i in range(len(l)):
            dp.append([0,0])

        for idx, i in enumerate(l):
            eq = 1 if i in digits else 0
            less = [j for j in digits if j < i]
            # print(f"idx:{idx}; i:{i}; eq:{eq}; less:{less}")
            if idx == 0:
                if eq:
                    dp[idx][0] = 1   # special
                dp[idx][1] = len(less)  # any number can append
            else:
                # if dp[idx-1][0] == 0:   # last is not special
                #     dp[idx][1] = length * dp[idx-1][1]
                # else:
                dp[idx][0] = eq * dp[idx-1][0]
                dp[idx][1] = dp[idx-1][1] * length + len(less) * dp[idx-1][0]
            # print(dp)
        return sum(dp[-1]) + ret
