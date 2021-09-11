# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/11 14:04
# File: 0014.py
# Desc: 


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        leng = min([len(i) for i in strs])  if strs else 0
        for i in range(leng):
            s1 = [j[i] for j in strs]
            if len(set(s1)) > 1: break
            string += s1[0]
        return string