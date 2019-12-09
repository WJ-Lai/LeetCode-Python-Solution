# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # 递归：时间复杂度O(n),空间复杂度O(n)
    # 迭代：时间复杂度O(n),空间复杂度O(n)

    # 递归：时间复杂度O(n),空间复杂度O(n)
    def invertTree1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    # 迭代：时间复杂度O(n),空间复杂度O(n)
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        queue = []
        queue.append(root)
        while queue:
            t = queue.pop(0)
            t.left, t.right = t.right, t.left
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
        return root