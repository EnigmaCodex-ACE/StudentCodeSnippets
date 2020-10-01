# Easy
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity : O(N)
# Space Complexity : O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        temp = head
        while temp:
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
        return prev