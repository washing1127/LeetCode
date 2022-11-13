# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/13 17:48
# File: 0791.py
# Desc: 


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if not i in order: order+=i
        return ''.join(sorted(s, key=lambda x: order.index(x)))