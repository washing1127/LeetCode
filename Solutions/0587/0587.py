# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/04/23 11:40
# File: 0587.py
# Desc: 

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        dic = dict()
        max_x = max_y = 0
        min_x = min_y = 100
        for k, v in trees:
            max_x = max(max_x, k)
            max_y = max(max_y, v)
            min_x = min(min_x, k)
            min_y = min(min_y, v)
            if not k in dic: dic[k] = []
            dic[k].append(v)
        if min_x == max_x or min_y == max_y or len(trees) <= 2: return trees
        for k in dic.keys(): dic[k].sort()
        keys = sorted(dic.keys())
        zs = [keys[0], dic[keys[0]][-1]]
        zx = [keys[0], dic[keys[0]][0]]
        ret = []
        for key in keys:
            point = [key, dic[key][0]]
            if len(ret) < 2:
                ret.append(point)
                continue
            while len(ret) >= 2:
                fx1 = (ret[-1][1] - ret[-2][1]) / (ret[-1][0] - ret[-2][0])
                fx2 = (point[1] - ret[-2][1]) / (point[0] - ret[-2][0])
                if fx2 >= fx1:
                    break
                ret.pop()
            ret.append(point)
        ret2 = []
        for key in keys:
            point = [key, dic[key][-1]]
            if len(ret2) < 2:
                ret2.append(point)
                continue
            while len(ret2) >= 2:
                fx1 = (ret2[-1][1] - ret2[-2][1]) / (ret2[-1][0] - ret2[-2][0])
                fx2 = (point[1] - ret2[-2][1]) / (point[0] - ret2[-2][0])
                if fx2 <= fx1: break
                ret2.pop()
            ret2.append(point)
        for i in ret2:
            if not i in ret:
                ret.append(i)
        # print(min_x, max_x, min_y, max_y)
        for i in trees:
            if i[0] == max_x or i[0] == min_x or i[1] == max_y or i[1] == min_y:
                if not i in ret: ret.append(i)
        return ret
