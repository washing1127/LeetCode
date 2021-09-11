# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/25 11:00
# File: 0897.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        cur = root
        li = []
        def parse(cur):
            li.append(cur.val)
            if cur.left != None:
                parse(cur.left)
            if cur.right != None:
                parse(cur.right)
        parse(cur)
        li.sort()
        ret = TreeNode(li[0])
        cur2 = ret
        for i in li[1:]:
            cur2.right = TreeNode(i)
            cur2 = cur2.right
        return ret