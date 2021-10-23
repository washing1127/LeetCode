# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/23 22:23
# File: 0492.py
# Desc: 

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        num = math.sqrt(area)
        if num == int(num): return [int(num), int(num)]
        num = int(num)+1
        while True:
            if area % num == 0:
                return [num, area//num]
            num += 1
