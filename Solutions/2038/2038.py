# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/22 9:15
# File: 2038.py
# Desc: 

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        dic = {'A': 0, 'B': 0}
        this = ""
        counter = 0
        colors += "C"
        for i in colors:
            if this == i: counter += 1
            else:
                if counter >= 3: dic[this] += counter-2
                counter = 1
                this = i
        return dic['A'] > dic['B']
