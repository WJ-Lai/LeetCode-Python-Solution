# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right

class Solution(object):

    # 递归：时间复杂度O(n),空间复杂度O(n)
    # 栈迭代：时间复杂度O(n),空间复杂度O(n)：与递归的思想类似，只是换成了栈去实现
    # 反序中序Morris遍历：时间复杂度O(n),空间复杂度O(1)：用修改指针的方法，太牛逼了。。

    # 递归：时间复杂度O(n),空间复杂度O(n)
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root

    # 栈迭代：时间复杂度O(n),空间复杂度O(n)
    def convertBST1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack, total, node = [], 0, root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        return root

    # 反序中序Morris遍历：时间复杂度O(n),空间复杂度O(1)
    def convertBST2(self, root):
        # 找到仅比node大的节点
        # 即右子树中的最小值
        def get_successor(node):
            succ = node.right
            while succ.left and succ.left is not node:
                succ = succ.left
            return succ
        total = 0
        node = root
        while node:
            # 若已经找到了未更新节点中的最大值
            if not node.right:
                # 节点更新
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = get_successor(node)
                if succ.left is None:
                    # 建立临时指针
                    succ.left = node
                    # 找下一指针的临时指针
                    node = node.right
                else:
                    # 删除临时指针
                    succ.left = None
                    # 节点更新
                    total += node.val
                    node.val = total
                    node = node.left
        return root



# if __name__ == '__main__':
#     s = Solution()
#     root = TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(13))
#     s.convertBST(root)
