# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/1 20:21
# File: 2325.py
# Desc: 

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {' ': ' '}
        idx = 97
        for k in key:
            if not k in d:
                d[k] = chr(idx)
                idx += 1
        ret = [d[i] for i in message]
        return ''.join(ret)
