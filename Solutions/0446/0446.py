# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/8/11 15:42
# File: 0446.py
# Desc: 

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        f = [defaultdict(int) for _ in nums]
        for i, x in enumerate(nums):
            for j in range(i):
                d = x - nums[j]
                cnt = f[j][d]
                ans += cnt
                f[i][d] += cnt + 1
        return ans
