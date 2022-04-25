# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/4/25 20:52
# File: 0398.py
# Desc: 

class Solution:

    def __init__(self, nums: List[int]):
        self.c = dict()
        for idx, num in enumerate(nums):
            if not num in self.c: self.c[num] = []
            self.c[num].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.c[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
