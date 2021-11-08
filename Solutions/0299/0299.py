# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/8 17:43
# File: 0299.py
# Desc: 


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        ls = list(secret)
        lg = list(guess)
        a = 0
        for i,j in zip(secret,guess):
            if i == j:
                ls.remove(i)
                lg.remove(j)
                a += 1
        b = 0
        for i in ls:
            if i in lg:
                b += 1
                lg.remove(i)
        return f"{a}A{b}B"
