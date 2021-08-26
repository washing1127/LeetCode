# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/27 10:42
# File: 0881.py
# Desc: 

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            if people[light] + people[heavy] > limit:
                heavy -= 1
            else:
                light += 1
                heavy -= 1
            ans += 1
        return ans
