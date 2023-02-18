# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/18 08:00
# File: 1237.py
# Desc: 

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ret = []
        r = 1000
        for x in range(1,1001):
            l = 1
            while l<r:
                y = (l+r)//2
                if customfunction.f(x,y) > z:
                    r = y
                if customfunction.f(x,y) < z:
                    l = y+1
                if customfunction.f(x,y) == z:
                    ret.append([x,y])
                    break
        return ret
