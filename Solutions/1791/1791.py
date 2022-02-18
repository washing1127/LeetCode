# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/18 10:47
# File: 1791.py
# Desc: 

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
