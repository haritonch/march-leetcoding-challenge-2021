# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length = 0
        p = p1 = p2 = head
        while p:
            length += 1
            p = p.next
        for i in range(k-1):
            p1 = p1.next
        for i in range(length-k):
            p2 = p2.next
        p1.val, p2.val = p2.val, p1.val
        return head
