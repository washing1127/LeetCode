# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/6 8:45
# File: 1423.py
# Desc: 
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[:k])
        max_num = total
        for i in range(k):
            total = total - cardPoints[k-i-1] + cardPoints[-i-1]
            if total > max_num:
                max_num = total
        return max_num