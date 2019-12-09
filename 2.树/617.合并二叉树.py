# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right

class Solution(object):

    # 递归：时间复杂度O(n),空间复杂度O(n)
    # 迭代：时间复杂度O(n),空间复杂度O(n)

    # 递归：时间复杂度O(n),空间复杂度O(n)
    def mergeTrees1(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1: return t2
        if not t2: return t1

        # 节点相加
        t1.val += t2.val

        # 递推
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

    # 迭代：时间复杂度O(n),空间复杂度O(n)
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 考虑特殊情况
        if not t1: return t2

        queue = []
        queue.append([t1, t2])
        while queue:
            t = queue.pop(0)
            # 考虑t2为None的情况，若为None，则直接为t1
            # 因为后续t2的子树仍然可能为空，所以不能省去
            if not t[1]:
                continue

            t[0].val += t[1].val

            # 将左树放入队列
            if not t[0].left:
                t[0].left = t[1].left
            else:
                queue.append([t[0].left, t[1].left])
            # 将右树放入队列
            if not t[0].right:
                t[0].right = t[1].right
            else:
                queue.append([t[0].right, t[1].right])

        return t1

# if __name__ == '__main__':
#     s = Solution()
#     t1 = TreeNode(1, TreeNode(3, 5), 2)
#     t2 = TreeNode(2, TreeNode(1, None, 4), TreeNode(3, None, 7))
#     s.mergeTrees(t1, t2)