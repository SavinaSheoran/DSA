# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0)
        root = head
        carry = 0
    #Loops
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry

            carry = s // 10
            head.next = ListNode(s % 10)
            head = head.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry:
            head.next = ListNode(carry)

        return root.next