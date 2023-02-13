# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/13 22:00
# File: 1234.py
# Desc: 

class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        partial = len(s) // 4

        def check():
            if cnt['Q'] > partial or \
                    cnt['W'] > partial or \
                    cnt['E'] > partial or \
                    cnt['R'] > partial:
                return False
            return True

        if check():
            return 0

        res = len(s)
        r = 0
        for l, c in enumerate(s):
            while r < len(s) and not check():
                cnt[s[r]] -= 1
                r += 1
            if not check():
                break
            res = min(res, r - l)
            cnt[c] += 1
        return res
