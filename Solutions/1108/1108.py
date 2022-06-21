# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/21 11:05
# File: 1108.py
# Desc: 

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
