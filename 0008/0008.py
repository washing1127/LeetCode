# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/01/01 23:40
# File: 0008.py
# Desc: 

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s: return 0
        ret = ''
        for i in s.strip():
            if not ret:
                if i in '-+1234567890':
                    ret += i
                else:
                    return 0
            else:
                if i in '1234567890':
                    ret += i
                else: break
        try:
            ret = int(ret)
        except:
            return 0
        if ret < -2 ** 31 : ret = -2 ** 31
        if ret > 2 ** 31 -1 : ret = 2 ** 31 -1
        return ret
