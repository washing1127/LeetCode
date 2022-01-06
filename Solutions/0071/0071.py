# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/6 10:52
# File: 0071.py
# Desc: 

class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        l2=[]
        for i in l:
            if not i or i == '.': continue
            elif i == '..': l2 = l2[:-1]
            else: l2.append(i)
        return '/' + '/'.join(l2)
