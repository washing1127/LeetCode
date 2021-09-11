# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/18 17:50
# File: 面试题 10.02.py
# Desc: 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for s in strs:
            k = "".join(sorted(s))
            if k not in dic.keys(): dic[k] = list()
            dic[k].append(s)
        return list(dic.values())
