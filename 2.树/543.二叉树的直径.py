# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):

    # 递归：时间复杂度O(n),空间复杂度O(n)
    def __init__(self):
        self.max_len = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def length(root):
            if not root: return 0
            llen = length(root.left)
            rlen = length(root.right)
            self.max_len = max(self.max_len, llen+rlen)
            return max(llen, rlen)+1

        length(root)
        return self.max_len

# if __name__ == '__main__':
#     s = Solution()
#     root = TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(13), TreeNode(13, TreeNode(13), TreeNode(13)))), TreeNode(13))
#     print(s.diameterOfBinaryTree(root))
