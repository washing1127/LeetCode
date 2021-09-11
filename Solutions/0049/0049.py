# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/14 11:20
# File: 0049.py
# Desc: 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for item in strs:
            k = ''.join(sorted(item))
            if not k in dic.keys(): dic[k] = []
            dic[k].append(item)
        return [i for i in dic.values()]
