# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/10 15:38
# File: 1629.py
# Desc: 

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = keysPressed[0]
        maxTime = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            key = keysPressed[i]
            time = releaseTimes[i] - releaseTimes[i - 1]
            if time > maxTime or time == maxTime and key > ans:
                ans = key
                maxTime = time
        return ans

