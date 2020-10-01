# Easy

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_list = ListNode()
        new_node = new_list
        temp = head
        while temp:
            nex = temp.next
            while nex and temp.val == nex.val:
                nex = nex.next
            new_node.next = ListNode(temp.val)
            new_node = new_node.next
            temp = nex
        return new_list.next