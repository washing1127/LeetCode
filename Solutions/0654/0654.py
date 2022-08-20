# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/20 09:49
# File: 0654.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def parse(l):
            if len(l) == 0:
                return None
            elif len(l) == 1:
                return TreeNode(l[0])
            else:
                max_num = max(l)
                idx = l.index(max_num)
                tn = TreeNode(max_num)
                tn.left = parse(l[:idx])
                tn.right = parse(l[idx+1:])
                return tn

        t = parse(nums)
        return t
