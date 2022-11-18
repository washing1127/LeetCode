# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/18 11:05
# File: 0891.py
# Desc: CV


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        MOD = 10 ** 9 + 7
        x, y = nums[0], 2
        for j in range(1, len(nums)):
            res = (res + nums[j] * (y - 1) - x) % MOD
            x = (x * 2 + nums[j]) % MOD
            y = y * 2 % MOD
        return (res + MOD) % MOD

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/sum-of-subsequence-widths/solutions/1976655/zi-xu-lie-kuan-du-zhi-he-by-leetcode-sol-649q/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
