# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/10 15:21
# File: 0413.py
# Desc: 

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        l1 = [] # 储存差值
        for idx, i in enumerate(nums[:-1]):
            j = nums[idx+1]
            l1.append(j-i)
        l2 = [1] # 储存出现次数
        last_cha = l1[0]
        for cha in l1[1:]:
            if cha == last_cha:
                l2[-1] += 1
            else: 
                last_cha = cha
                l2.append(1)
        ret = 0
        for i in l2:
            b = i - 1
            if b >= 1:
                ret += (1 + b) * (b) // 2

        return ret