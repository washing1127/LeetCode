# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/4 00:35
# File: 0781.py
# Desc: 

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if not answers: return 0
        ans = 0
        c = collections.Counter(answers)
        for k, v in c.items():
            print(k,v,ans)
            if v <= k+1:
                ans += k + 1
            else:  # v > k + 1
                if k == 0:
                    ans += v
                else:
                    ys = v % (k + 1)
                    if ys == 0:
                        ans += v
                    else:
                        ans += v - ys + k + 1
        return ans
