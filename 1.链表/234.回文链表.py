# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution(object):

    # 双指针+反转链表：时间复杂度O(n),空间复杂度O(1)
    # 数组法:头和尾同时向中间靠近：时间复杂度O(n),空间复杂度O(n)

    # 双指针+反转链表：时间复杂度O(n),空间复杂度O(1)
    def isPalindrome(self, head):
        if not (head and head.next): return True
        p = ListNode(-1)
        # p.next要指向head，否则low和fast的next为空
        p.next, slow, fast = head, p, p
        # 找到中点
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # 链表反转
        # 需要反转的链表从low的下一个开始
        cur, pre = slow.next, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        # 判断两个链表是否相等
        # a, b = p.next, pre也可以
        a, b = head, pre
        while b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return True

    # 数组法:头和尾同时向中间靠近：时间复杂度O(n),空间复杂度O(n)
    def isPalindrome3(self, head):
        if not (head and head.next): return True

        arr, i = [], 0
        while head:
            _, head = arr.append(head.val), head.next
        j = len(arr)-1
        while i<j:
            if arr[i] != arr[j]:
                return False
            i, j = i+1, j-1
        return True

l = ListNode(1, ListNode(2))
print(Solution().isPalindrome2(l))