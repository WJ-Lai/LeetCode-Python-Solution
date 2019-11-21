# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x, next=None):
#         self.val = x
#         self.next = next

class Solution(object):

    # 暴力法：对于A中每一个节点，都遍历一次B中所有节点，时间复杂度O(mn)，空间复杂度O(1)
    # 哈希表法：将A所有节点存在哈希表中，检查B中每一个节点是否在A中，时间复杂度O(m+n)，空间复杂度O(m)/O(n)
    # 双指针法：A自己+重叠+B自己=B自己+重叠+A自己
    # 双指针法具体流程：
    # 指针pA遍历完链表A后跳到链表B继续遍历，指针pB遍历完链表B后跳链表A继续遍历
    # 若有重复的指针，则会出现相等的情况，若没有重复的话，则每一次的pA和pB都是不等的
    # 若无重叠的话，A自己+B自己 = B自己+A自己
    # 若有重叠的话，A自己+重叠+B自己=B自己+重叠+A自己，则下一个必为重叠开头的元素

    # 双指针法
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        preHeadA, preHeadB = headA, headB
        while preHeadA != preHeadB:
            preHeadA = preHeadA.next if preHeadA else headB
            preHeadB = preHeadB.next if preHeadB else headA
        return preHeadA

    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 哈希表法
        hashIDs = {}
        while headA:
            hashIDs[id(headA)] = 1
            headA = headA.next
        while headB:
            if id(headB) in hashIDs:
                return headB
            headB = headB.next
        return None
