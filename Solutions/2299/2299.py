# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/19 10:21
# File: 2299.py
# Desc: 


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        ret = [0,0,0,0,0,1]
        if len(password) >= 8: ret[0] = 1
        for idx,i in enumerate(password):
            if i.islower(): ret[1] = 1
            elif i.isupper(): ret[2] = 1
            elif i.isdigit(): ret[3] = 1
            elif i in "!@#$%^&*()-+": ret[4] = 1
            if idx > 0 and password[idx-1] == i: ret[5] = 0
        return 0 not in ret
