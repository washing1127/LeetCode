# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/6 11:30
# File: 1408.py
# Desc: 


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [i for i in words if '|'.join(words).count(i) >= 2]
