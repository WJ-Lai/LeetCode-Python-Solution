# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x, next=None):
#         self.val = x
#         self.next = next

class Solution(object):

    # 递归法，时间复杂度O(m+n)，空间复杂度O(m+n)
    # 迭代法，时间复杂度O(m+n)，空间复杂度O(1)

    # 递归法，时间复杂度O(m+n)，空间复杂度O(m+n)
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # 迭代法，时间复杂度O(m+n)，空间复杂度O(1)
    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val < l2.val:
                prev.next, l1 = l1, l1.next
            else:
                prev.next, l2 = l2, l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return prehead.next

# l1=ListNode(1,next=ListNode(2,next=ListNode(3)))
# l2=ListNode(4,next=ListNode(5,next=ListNode(6)))
# s = Solution()
# head = s.mergeTwoLists(l1, l2)
# print(head)
