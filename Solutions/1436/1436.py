# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/1 21:53
# File: 1436.py
# Desc: 
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = dict()
        for k, v in paths:
            dic[k] = v
        for v in dic.values():
            if not v in dic.keys(): return v
