# leetcode 114
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# in place solution
class Solution: 
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre_right=None
        def helper(root=root):
            if root:
                helper(root.right)
                helper(root.left)
                root.right=self.pre_right
                self.pre_right=root
                root.left=None
        helper()
