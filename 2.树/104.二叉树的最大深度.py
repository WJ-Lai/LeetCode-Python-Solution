# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # 递归：时间复杂度O(n),空间复杂度O(logn)
    # 迭代：时间复杂度O(n),空间复杂度O(n)：栈同时存放节点的深度和节点

    # 递归：时间复杂度O(n),空间复杂度O(logn)
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if not root else max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)

    # 迭代：时间复杂度O(n),空间复杂度O(n)
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        stack, depth = [], 0
        stack.append((1, root))
        while stack:
            cur_depth, root = stack.pop()
            if root:
                depth = max(depth, cur_depth)
                stack.append((cur_depth+1, root.left))
                stack.append((cur_depth+1, root.right))
        return depth