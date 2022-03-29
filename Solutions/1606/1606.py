# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/25 11:15
# File: 1609.py
# Desc: CV

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            prev = float('inf') if level % 2 else 0
            nxt = []
            for node in queue:
                val = node.val
                if val % 2 == level % 2 or level % 2 == 0 and val <= prev or level % 2 == 1 and val >= prev:
                    return False
                prev = val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
            level += 1
        return True

