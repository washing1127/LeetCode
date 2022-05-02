# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/4/3 10:10
# File: 0937.py
# Desc: 

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log: str) -> tuple:
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1,)

        logs.sort(key=trans)  # sort 是稳定排序
        return logs

