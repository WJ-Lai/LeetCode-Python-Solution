class Solution(object):
    # 迭代：时间复杂度O(n),空间复杂度O(n)
    # 递归：时间复杂度O(n),空间复杂度O(n)

    # 迭代
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            next_queue = []
            leaf_val = []
            for node in queue:
                if not node:
                    leaf_val.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)
                leaf_val.append(node.val)
            queue = next_queue
            if leaf_val!=leaf_val[::-1]:
                return False
        return True

    # 递归
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False

            if node1.val!=node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        return check(root, root)
