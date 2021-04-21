# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/4/21 17:48
desc: 0091.py
"""
class Solution:
    def numDecodings(self, s: str) -> int:
    
        def fib(n):
            a = 1
            b = 2
            for i in range(1, n):
                a, b = b, a+b
            return a

        def compute(s):
            s = s.replace("/", "/ ")
            l = [i for i in s.split(" ") if i != ""]
            l2 = [fib(len(i)) for i in l]
            ret = 1
            for i in l2: ret *= i
            return ret

        for i in range(len(s)):
            if s[i] == "0":
                if i == 0: return 0
                elif s[i-1] not in "12": return 0
                else:
                    s = s[:i-1] + "||" + s[i+1:]
            elif s[i] in "789":
                if i == 0 or not s[i-1] == "1":
                    c = "|"
                else: c = "/"
                s = s[:i] + c + s[i+1:]
        for i in "3456": s = s.replace(i, "/")
        l = [i for i in s.split("|") if i not in "/"]
        l = [compute(i) for i in l]

        ret = 1
        for i in l: ret *= i 
        return ret
