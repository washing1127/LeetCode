# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/27 10:10
# File: 0938.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ret = 0
        
        def parse(cur):
            if low <= cur.val <= high:
                self.ret += cur.val
            if cur.left != None: parse(cur.left)
            if cur.right != None: parse(cur.right)

        parse(root)

        return self.ret