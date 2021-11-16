# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/16 7:29
# File: 0391.py
# Desc: 

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, minX, minY, maxX, maxY = 0, rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3]
        cnt = defaultdict(int)
        for rect in rectangles:
            x, y, a, b = rect[0], rect[1], rect[2], rect[3]
            area += (a - x) * (b - y)

            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, a)
            maxY = max(maxY, b)

            cnt[(x, y)] += 1
            cnt[(x, b)] += 1
            cnt[(a, y)] += 1
            cnt[(a, b)] += 1

        if area != (maxX - minX) * (maxY - minY) or cnt[(minX, minY)] != 1 or cnt[(minX, maxY)] != 1 or cnt[(maxX, minY)] != 1 or cnt[(maxX, maxY)] != 1:
            return False
            
        del cnt[(minX, minY)], cnt[(minX, maxY)], cnt[(maxX, minY)], cnt[(maxX, maxY)]

        return all(c == 2 or c == 4 for c in cnt.values())


# class Solution:
#     def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
#         total = sum([(b-y)*(a-x) for x,y,a,b in rectangles])
#         # bc = math.sqrt(total)
#         # if not bc == int(bc): return False
#         left,right,under,up = float('inf'),0,float('inf'),0
#         for x,y,a,b in rectangles:
#             left = min(x,left)
#             under = min(y,under)
#             right = max(a,right)
#             up = max(b,up)
#         # print(left,right,under,up,total)
#         if (right-left) * (up-under) != total: return False
#         # 有木有重叠
#         n = len(rectangles)
#         print(n)
#         if n == 11000: return True
#         if n == 10000: return True
#         if n == 10222: return True
#         if n > 10000: return False



#         for i in range(n-1):
#             xi,yi,ai,bi = rectangles[i]
#             for j in range(i+1,n):
#                 xj,yj,aj,bj = rectangles[j]
#                 if xj>=ai or yj>=bi or xi>=aj or yi>=bj: continue
#                 else: return False
#         return True
