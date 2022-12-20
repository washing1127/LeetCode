# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/20 10:03
# File: 1760.py
# Desc: CV


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right, ans = 1, max(nums), 0
        while left <= right:
            y = (left + right) // 2
            ops = sum((x - 1) // y for x in nums)
            if ops <= maxOperations:
                ans = y
                right = y - 1
            else:
                left = y + 1

        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/solutions/2025611/dai-zi-li-zui-shao-shu-mu-de-qiu-by-leet-boay/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
