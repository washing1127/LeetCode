# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/26 16:50
# File: 0700.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        while cur:
            if cur.val == val: return cur
            elif cur.val < val: cur = cur.right
            else: cur = cur.left
        return cur
