# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/30 10:42
# File: 1175.py
# Desc: 

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        priList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,]
        zs = 0
        for i in priList:
            if i <= n: zs+=1
            else: break
        ss = n - zs
        return (factorial(zs)*factorial(ss)) % (10**9+7)
