# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/21 10:52
# File: 0401.py
# Desc: 

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans

