# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/5 18:11
# File: 0478.py
# Desc: CV



class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.xc = x_center
        self.yc = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        u, theta = random.random(), random.random() * 2 * math.pi
        r = sqrt(u)
        return [self.xc + r * math.cos(theta) * self.r, self.yc + r * math.sin(theta) * self.r]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
