# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/28 17:58
# File: 0028.py
# Desc: 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        ret = -1
        for i in range(len(haystack)-len(needle)+1):
            if needle == haystack[i:i+len(needle)]: return i
        return ret
