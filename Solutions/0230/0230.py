# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l = []

        def parse(root):
            self.l.append(root.val)
            if root.left: parse(root.left)
            if root.right: parse(root.right)
        
        parse(root)

        self.l.sort()
        return self.l[k-1]
