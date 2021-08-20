# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/20 10:51
# File: 0541.py
# Desc: 

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ret = ''
        counter = 0
        fx = -1
        temp = ''
        for i in s:
            counter += 1
            temp += i
            if counter == k:
                ret += temp[::fx]
                fx *= -1
                temp = ''
                counter = 0
        
        ret += temp[::fx]
        return ret