# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/6 10:52
# File: 0927.py
# Desc: CV


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        s = sum(arr)
        if s % 3:
            return [-1, -1]
        if s == 0:
            return [0, 2]

        partial = s // 3
        first = second = third = cur = 0
        for i, x in enumerate(arr):
            if x:
                if cur == 0:
                    first = i
                elif cur == partial:
                    second = i
                elif cur == 2 * partial:
                    third = i
                cur += 1

        n = len(arr)
        length = n - third
        if first + length <= second and second + length <= third:
            i = 0
            while third + i < n:
                if arr[first + i] != arr[second + i] or arr[first + i] != arr[third + i]:
                    return [-1, -1]
                i += 1
            return [first + length - 1, second + length]
        return [-1, -1]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/three-equal-parts/solution/san-deng-fen-by-leetcode-solution-3l2y/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
