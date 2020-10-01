# Easy
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: # If the list is empty
            return True
        
        slow, fast = head, head
        #   Finding Midptr   
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # Reversing from middleptr         
        prev, temp = None, slow
        while temp:
            nex = temp.next
            temp.next = prev
            prev = temp
            temp = nex
        # Now prev will be the head ptr which is the last node after reversing       
        while head:
            if head.val != prev.val:
                return False
            head, prev = head.next, prev.next
        return True