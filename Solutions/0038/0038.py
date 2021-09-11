# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/30 19:05
# File: 0038.py
# Desc: 

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'

        def count(num):
            klist = []
            for i in str(num):
                if not klist or i not in klist[-1].keys():
                    klist.append({i: 1})
                else:
                    klist[-1][i] += 1
            s = ''
            for i in klist:
                for k, v in i.items():
                    s += f"{v}{k}"
            return int(s)

        num = 1
        for i in range(n - 1):
            num = count(num)
        return str(num)
