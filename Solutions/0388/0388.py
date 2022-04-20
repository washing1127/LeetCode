# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/4/20 7:29
# File: 0388.py
# Desc: 

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = []
        max_length = 0
        ret = 0
        for i in input.split("\n"):
            l = i.split("\t")
            lines.append(l)
            max_length = max(max_length, len(l))
        path_list = [''] * max_length
        for line in lines:
            i = len(line)-1
            path_list[i] = line[i]
            if '.' in line[-1]:
                ret = max(ret, len("/".join(path_list[:i+1])))
        # print(path_list)
        return ret
