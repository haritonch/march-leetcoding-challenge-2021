"""Problem found at
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3660/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self, head):
            ans = 0
            p = head
            while p:
                ans += 1
                p = p.next
            return ans
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nA = length(headA)
        nB = length(headB)
        pA = headA
        pB = headB
        if nA > nB:
            for _ in range(nA - nB):
                nA -= 1
                pA = pA.next
        elif nA < nB:
            for _ in range(nB - nA):
                pB = pB.next
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA