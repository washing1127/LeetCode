# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/04/28 16:51
# File: 0417.py
# Desc: 

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        l1 = []
        l2 = []
        ret = []
        m = len(heights)
        n = len(heights[0])
        for _ in heights:
            l1.append([0] * n)
            l2.append([0] * n)
        def parse(point):
            x,y = point
            if l[x][y] == 1:
                if x>0 and l[x-1][y] == 0 and heights[x-1][y] >= heights[x][y]:
                    l[x-1][y] += 1
                    parse((x-1, y))
                if y>0 and l[x][y-1] == 0 and heights[x][y-1] >= heights[x][y]:
                    l[x][y-1] += 1
                    parse((x, y-1))
                if x<m-1 and l[x+1][y] == 0 and heights[x+1][y] >= heights[x][y]:
                    l[x+1][y] += 1
                    parse((x+1, y))
                if y<n-1 and l[x][y+1] == 0 and heights[x][y+1] >= heights[x][y]:
                    l[x][y+1] += 1
                    parse((x, y+1))
        l = l1
        for x, li in enumerate(heights):
            for y, num in enumerate(heights[0]):
                point = (x,y)
                if x == 0 or y == 0: l[x][y] = 1
                parse(point)
        l = l2
        for x, li in enumerate(heights):
            for y, num in enumerate(heights[0]):
                point = (x,y)
                if x == m-1 or y == n-1: l[x][y] = 1
                parse(point)
        for x in range(m):
            for y in range(n):
                if l1[x][y] and l2[x][y]:
                    ret.append([x,y])
        return ret
        # for i in l1:
        #     print(i)
        # print("----------")
        # for i in l2:
        #     print(i)
