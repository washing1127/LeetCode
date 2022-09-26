# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/3 14:07
# File: ������17.19.py
# Desc: CV


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        xorsum = 0
        n = len(nums) + 2
        for num in nums:
            xorsum ^= num
        for i in range(1, n + 1):
            xorsum ^= i

        lsb = xorsum & (-xorsum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        for i in range(1, n + 1):
            if i & lsb:
                type1 ^= i
            else:
                type2 ^= i

        return [type1, type2]

# ���ߣ�LeetCode-Solution
# ���ӣ�https://leetcode.cn/problems/missing-two-lcci/solution/xiao-shi-de-liang-ge-shu-zi-by-leetcode-zuwq3/
# ��Դ�����ۣ�LeetCode��
# ����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������
