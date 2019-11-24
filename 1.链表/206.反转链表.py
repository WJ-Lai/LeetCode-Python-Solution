# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x, next=None):
#         self.val = x
#         self.next = next


class Solution(object):

    # 迭代法，时间复杂度O(n)，空间复杂度O(1)
    # 递归法，时间复杂度O(n)，空间复杂度O(n)
    # 递归思路
    # 若第1~k个节点还没改好，后面的第k+1~m个节点已经改好，那么对于第k个节点要进行的更改公式就是nk.next.next=nk

    # 迭代法，时间复杂度O(n)，空间复杂度O(1)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    # 递归法，时间复杂度O(n)，空间复杂度O(n)
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next): return head
        # p相当于是为了记录最后一个节点的位置，便于return
        p = self.reverseList1(head.next)
        # 别忘了第一个指针要指向None
        # 实际上每一次递归后，最左侧的节点都会被改为指向None，即完成当前链表的反转
        # 然后回到上一次递归后，head.next.next将节点从None指向更左边的指针
        head.next.next, head.next = head, None
        return p


# l1 = ListNode(1, next=ListNode(2, next=ListNode(3)))
# s = Solution()
# ss = s.reverseList1(l1)
# print()
