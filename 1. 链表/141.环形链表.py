# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False

        l_fast, l_slow = head, head

        while l_fast.next:
            l_fast, l_slow = l_fast.next, l_slow.next
            if not l_fast.next:
                break
            elif l_slow is l_fast.next:
                return True
            else:
                l_fast = l_fast.next
        return False
