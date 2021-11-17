# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/17 20:37
# File: 0563.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache
    def findTilt(self, root: TreeNode) -> int:
        def get_he(node):
            he = node.val
            if node.left: 
                he += get_he(node.left)
            if node.right: 
                he += get_he(node.right)
            return he
        
        self.ret = 0
        def get_pd(node):
            left = get_he(node.left) if node.left else 0
            right = get_he(node.right) if node.right else 0
            self.ret += abs(left - right)
            if node.left: get_pd(node.left)
            if node.right: get_pd(node.right)

        if root: get_pd(root)

        return self.ret
