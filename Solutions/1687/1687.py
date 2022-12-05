# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/5 10:10
# File: 1687.py
# Desc: 


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        def getArray() -> List[int]:
            return [0] * (n + 1)

        n = len(boxes)
        p, w, neg, W = getArray(), getArray(), getArray(), getArray()

        for i in range(1, n + 1):
            p[i], w[i] = boxes[i - 1]
            if i > 1:
                neg[i] = neg[i - 1] + (p[i - 1] != p[i])
            W[i] = W[i - 1] + w[i]

        opt = deque([0])
        f, g = getArray(), getArray()

        for i in range(1, n + 1):
            while i - opt[0] > maxBoxes or W[i] - W[opt[0]] > maxWeight:
                opt.popleft()

            f[i] = g[opt[0]] + neg[i] + 2

            if i != n:
                g[i] = f[i] - neg[i + 1]
                while opt and g[i] <= g[opt[-1]]:
                    opt.pop()
                opt.append(i)

        return f[n]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/delivering-boxes-from-storage-to-ports/solutions/2005717/cong-cang-ku-dao-ma-tou-yun-shu-xiang-zi-4uya/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
