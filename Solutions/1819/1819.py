# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/14 21:37
# File: 1819.py
# Desc: 


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        maxVal = max(nums)
        occured = [False] * (maxVal + 1)
        for num in nums:
            occured[num] = True
        ans = 0
        for i in range(1, maxVal + 1):
            subGcd = 0
            for j in range(i, maxVal + 1, i):
                if occured[j]:
                    if subGcd == 0:
                        subGcd = j
                    else:
                        subGcd = gcd(subGcd, j)
                    if subGcd == i:
                        ans += 1
                        break
        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/number-of-different-subsequences-gcds/solutions/2060230/xu-lie-zhong-bu-tong-zui-da-gong-yue-shu-ha1j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
