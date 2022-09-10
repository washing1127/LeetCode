# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/10 10:28
# File: 0669.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def parse(root):
            if not root: return None
            if not root.left and not root.right:
                if low <= root.val <= high: return root
                else: return None
            left = right = None
            if root.left: left = parse(root.left)
            if root.right: right = parse(root.right)
            if low <= root.val <= high:
                root.left = left
                root.right = right
                return root
            else:
                if left: return left
                else: return right
            
        return parse(root)


