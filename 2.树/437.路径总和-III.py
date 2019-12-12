# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # 栈：时间复杂度O(),空间复杂度O()
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        stack, res = [], 0
        stack.append([root, [root.val]])

        while stack:
            node, his_val = stack.pop()
            res += his_val.count(sum)
            # 太牛逼了扩展维度
            his_val += [0]
            if node.left:
                stack.append([node.left, [node.left.val+val for val in his_val]])
            if node.right:
                stack.append([node.right, [node.right.val+val for val in his_val]])
        return res

