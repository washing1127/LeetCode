# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/5 10:10
# File: 1576.py
# Desc: 

class Solution:
    def modifyString(self, s: str) -> str:
        l = list(s)
        for i in range(len(l)):
            if l[i] == "?":
                if i==0:
                    a=0;b=i+2
                else:
                    a=i-1;b=i+2
                if "a" not in l[a:b]: l[i] = "a"
                elif "b" not in l[a:b]: l[i] = "b"
                elif "c" not in l[a:b]: l[i] = "c"
        return ''.join(l)
