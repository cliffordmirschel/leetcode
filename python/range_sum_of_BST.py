# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# First Attempt
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        def helper(node):
            if node is None:
                return
            print(node.val)
            if node.val >= low and node.val <= high:
                self.res += node.val
            helper(node.left)
            helper(node.right)
        helper(root)
        return self.res

class Solution:
    def range_sum_BST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        if not root:
            return 0
        if root.val > low:
            ans += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            ans += self.rangeSumBST(root.right, low, high)
        
        if low <= root.val <= high:
            ans += root.val
        return ans