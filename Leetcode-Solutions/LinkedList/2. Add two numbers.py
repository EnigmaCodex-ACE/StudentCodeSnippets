# Medium
# https://leetcode.com/problems/add-two-numbers/solution/

# Definition for singly-linked list.

# Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.

# Space complexity : O(max(m,n)). The length of the new list is at most max(m,n)+1.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        temp = res
        carry = 0
        while l1 or l2:
            if not l1:
                l1 = ListNode()
            elif not l2:
                l2 = ListNode()
            s = l1.val + l2.val + carry
            carry = s // 10
            temp.val = s % 10
            if l1.next or l2.next or carry > 0:
                temp.next = ListNode(carry)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        return res