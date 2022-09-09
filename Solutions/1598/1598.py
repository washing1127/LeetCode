# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/9 10:33
# File: 1598.py
# Desc: 

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        idx = 0
        while idx < len(logs):
            temp = logs[idx]
            if temp == './': logs.pop(idx)
            elif temp == "../":
                if idx > 0:
                    logs.pop(idx-1)
                    logs.pop(idx-1)
                    idx -= 1
                else:
                    logs.pop(idx)
            else:
                idx += 1
        return len(logs)

