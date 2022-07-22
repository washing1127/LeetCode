# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/24 10:40
# File: 1184.py
# Desc: 


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # return min(sum(distance[min(start, destination): max(start, destination)]), sum(distance)-sum(distance[min(start, destination): max(start, destination)]))
        if start > destination: start, destination = destination, start
        s1 = sum(distance)
        s2 = sum(distance[start: destination])
        return min(s2, s1-s2)
