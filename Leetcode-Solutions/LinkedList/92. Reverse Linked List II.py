# Medium
# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity : O(N)
# Space Complexity : O(1) using Four Pointers iterative solution
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:        
        ancestor, temp = None, head
        c = 1
        while c < m:
            ancestor = temp
            temp = temp.next
            c += 1
#         Now, ancestor points to the node m - 1
        prev, temp = temp, temp.next
        while c < n:
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
            c += 1
        if ancestor: # if m > 1
            # making m node next point to n.next             
            ancestor.next.next = temp
            ancestor.next = prev
        else: 
            head.next = temp
            head = prev
        return head