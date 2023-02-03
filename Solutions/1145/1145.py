# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/3 18:12
# File: 1145.py
# Desc: 

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        xNode = None

        def getSubtreeSize(node):
            if not node:
                return 0
            if node.val == x:
                nonlocal xNode
                xNode = node
            return 1 + getSubtreeSize(node.left) + getSubtreeSize(node.right)

        getSubtreeSize(root)
        leftSize = getSubtreeSize(xNode.left)
        if leftSize >= (n + 1) // 2:
            return True
        rightSize = getSubtreeSize(xNode.right)
        if rightSize >= (n + 1) // 2:
            return True
        remain = n - leftSize - rightSize - 1
        return remain >= (n + 1) // 2
