# Medium

# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = None
        temp = head
        prev_two = None
        while temp:
            prev_two = prev
            prev = temp
            temp = temp.next
            if temp:
                nex = temp.next
                temp.next = prev
                prev.next = nex
                if prev_two:
                    prev_two.next = temp
                else:
                    head = temp
                temp = nex
        return head
            
                