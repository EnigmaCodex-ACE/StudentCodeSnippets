# Medium
# https://leetcode.com/problems/path-sum-ii/submissions/

# DFS
# Time Complexity: O(N)
# Space Complexity: O(tree height)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def explore(self, node, s, target, cur_path, out):
        s += node.val
        cur_path.append(node.val)
        if not node.left and not node.right:
            if s == target:
                out.append(cur_path[::])
        else:
            if node.left:
                self.explore(node.left, s, target, cur_path, out)
                    
            if node.right:
                self.explore(node.right, s, target, cur_path, out)
                    
        cur_path.pop()
        s -= node.val
        
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        out = []
        self.explore(root, 0, sum, [], out)
        return out