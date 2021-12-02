# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/2 12:55
# File: 0506.py
# Desc: 

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l = sorted(score,reverse=True)
        for i in range(len(score)):
            mc = l.index(score[i]) + 1
            if mc == 1:
                score[i] = "Gold Medal"
            elif mc == 2:
                score[i] = "Silver Medal"
            elif mc == 3:
                score[i] = "Bronze Medal"
            else: score[i] = str(mc)
        return score
