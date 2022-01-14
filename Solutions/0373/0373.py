# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/14 10:45
# File: 0373.py
# Desc: 

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1 = nums1[:k]
        n2 = nums2[:k]
        dic = dict()
        for i in n1:
            for j in n2:
                if i+j not in dic: dic[i+j]=[[i,j]]
                else: dic[i+j].append([i,j])
        ret = []
        keys = sorted(dic.keys())
        for key in keys:
            ret.extend(dic[key])
            if len(ret) > k: break
        return ret[:k]
