# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/28 10:21
# File: 1331.py
# Desc: 


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l = sorted(list(set(arr)))
        dic = {num:idx+1 for idx, num in enumerate(l)}
        return [dic[num] for num in arr]
