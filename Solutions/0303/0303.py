# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/1 8:33
# File: 0303.py
# Desc: 

class NumArray:

    def __init__(self, nums: List[int]):
        self.li = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.li[i: j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)