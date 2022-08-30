# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/08/30 15:11
# File: 0998.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        t = TreeNode(val)
        if root.val < val:
            t.left = root
            return t
        cur = root
        while cur:
            if not cur.right:
                cur.right = t
                break
            elif cur.right.val < val:
                t.left = cur.right
                cur.right = t
                break
            cur = cur.right
        return root
