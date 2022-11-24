# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/24 11:32
# File: 0795.py
# Desc: 

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        l = []
        temp = []
        ma = 0
        for i in nums:
            if i > right:
                if ma >= left and temp:
                    l.append(temp)
                    ma = 0
                temp = []
            else:
                if i > ma: ma = i
                temp.append(i)
        if ma >= left and temp: l.append(temp)
        ret = 0
        for l2 in l:
            num = (len(l2)+1)*len(l2)//2
            temp = 0
            for i in l2:
                if i < left: temp += 1
                else:
                    if temp:
                        num -= (temp+1)*temp//2
                        temp = 0
            if temp: num -= (temp+1)*temp//2
            ret += num
        return ret
