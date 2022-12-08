# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/8 10:50
# File: 1812.py
# Desc: 


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return ord(coordinates[0])%2 != ord(coordinates[1])%2
