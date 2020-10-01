# Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N) and Space Complexity: O(N) where n = number of nodes in the tree
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        else:
            q = [root]
            out = [[root.val]]
            while q:
                size = len(q)
                out.append([])
                for _ in range(size):
                    ele = q.pop(0)
                    if ele.left:
                        out[-1].append(ele.left.val)
                        q.append(ele.left)
                    if ele.right:
                        out[-1].append(ele.right.val)
                        q.append(ele.right)
                if not out[-1]:
                    out.pop()
            return out