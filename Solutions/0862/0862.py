# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/26 15:28
# File: 0862.py
# Desc: CV


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSumArr = [0]
        res = len(nums) + 1
        for num in nums:
            preSumArr.append(preSumArr[-1] + num)
        q = deque()
        for i, curSum in enumerate(preSumArr):
            while q and curSum - preSumArr[q[0]] >= k:
                res = min(res, i - q.popleft())
            while q and preSumArr[q[-1]] >= curSum:
                q.pop()
            q.append(i)
        return res if res < len(nums) + 1 else -1

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/solution/he-zhi-shao-wei-k-de-zui-duan-zi-shu-zu-57ffq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
