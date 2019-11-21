# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    # 双指针法，时间复杂度O(n)，空间复杂度O(n)
    # 哈希表法，时间复杂度O(n)，空间复杂度O(1)
    # 修改数据法，一个指针遍历，每到一个地方val改为None，时间复杂度O(n)，空间复杂度O(1)
    # 限时法/限数法，限制遍历指针的时间/数量，超过阈值则认为有环

    # 双指针法，时间复杂度O(n)，空间复杂度O(n)
    def hasCycle(self, head):
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

    # 哈希表法，时间复杂度O(n)，空间复杂度O(1)
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False

        list_node = []

        while head:
            if head in list_node:
                return True
            else:
                list_node.append(head)
            head = head.next
        return False

