# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/13 10:35
# File: 1832.py
# Desc: 

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
