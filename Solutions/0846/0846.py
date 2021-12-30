# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/30 10:01
# File: 0846.py
# Desc: 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        while hand:
            first = hand[0]
            for i in range(groupSize):
                if first+i in hand: hand.remove(first+i)
                else: return False
        return True
