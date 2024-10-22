# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []  
        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                ans.append(node.val)
                inorder(node.right)
        inorder(root) 
        return ans