# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/7 10:49
# File: 1604.py
# Desc: 


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        timeMap = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, minute = int(time[:2]), int(time[3:])
            timeMap[name].append(hour * 60 + minute)

        ans = []
        for name, times in timeMap.items():
            times.sort()
            if any(t2 - t1 <= 60 for t1, t2 in zip(times, times[2:])):
                ans.append(name)
        ans.sort()
        return ans

