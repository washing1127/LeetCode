# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/21 10:18
# File: 0814.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def parse(root):
            if not root.left and not root.right:
                return root.val
            else:
                l = r = 0
                if root.left:
                    l = parse(root.left)
                    if l == 0: root.left = None
                if root.right:
                    r = parse(root.right)
                    if r == 0: root.right = None
                return max(root.val, l, r)
        ans = parse(root)
        if ans == 0: return
        return root
