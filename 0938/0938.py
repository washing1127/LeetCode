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
            num = cur.val
            if low <= num <= high:
                self.ret += num
            if num > low and cur.left != None: parse(cur.left)
            if num < high and cur.right != None: parse(cur.right)

        parse(root)

        return self.ret