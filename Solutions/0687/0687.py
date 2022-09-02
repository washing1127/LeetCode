# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/2 10:18
# File: 0687.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        def parse(root):
            nlv = None
            nrv = None
            nls = 0
            nrs = 0
            tls = 0
            trs = 0
            if root.left:
                nlv, nls = parse(root.left)
            if root.right:
                nrv, nrs = parse(root.right)
            if root.val == nlv:
                tls = nls+1
            if root.val == nrv:
                trs += nrs+1
            self.ret = max(self.ret, tls+trs)
            return root.val, max(tls, trs)
        if root: parse(root)
        return self.ret
