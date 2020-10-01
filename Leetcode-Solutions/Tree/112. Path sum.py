# Easy
# https://leetcode.com/problems/path-sum/submissions/

# DFS
# Time Complexity : O(N)
# Space Complexity: O(treeheight)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def explore(self, node, s, target):
        s += node.val
        if not node.left and not node.right:
            if s == target:
                return 1
        else:
            if node.left:
                if self.explore(node.left, s, target):
                    return 1
            if node.right:
                if self.explore(node.right, s, target):
                    return 1
        s -= node.val
    
    
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return 0
        return self.explore(root, 0, sum)