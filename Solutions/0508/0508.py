# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/18 12:55
# File: 0508.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.d = dict()
        def parse(root):
            left = 0
            right = 0
            if root.left:
                left = parse(root.left)
            if root.right:
                right = parse(root.right)
            val = root.val + left + right
            if val in self.d: self.d[val] += 1
            else: self.d[val] = 1
            return val
        parse(root)
        m = max(self.d.values())
        return [i for i,j in self.d.items() if j == m]
