# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/13 22:48
# File: 0768.py
# Desc: CV


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = Counter()
        res = 0
        for x, y in zip(arr, sorted(arr)):
            cnt[x] += 1
            if cnt[x] == 0:
                del cnt[x]
            cnt[y] -= 1
            if cnt[y] == 0:
                del cnt[y]
            if len(cnt) == 0:
                res += 1
        return res

