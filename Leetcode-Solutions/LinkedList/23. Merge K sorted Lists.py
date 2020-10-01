# Hard
# https://leetcode.com/problems/merge-k-sorted-lists/solution/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ---------------------------------------------------------------------------------------
# Solution Using Priority queue 
# Time Complexity : O( N log(k)) where k is the number of linked lists 
# and N is the total number of elements in the final sorted linked list

# Space complexity :

# O(n) Creating a new linked list costs O(n) space.
# O(k) the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations).

from queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
# ---------------------------------------------------------------------------------------

# Bruteforce
# Solution which extracts values from all the lists and sorts in place and creates a new linked list
# Time Complexity : O(N log N) - where N is the total number of elements in the final sorted linked list
# Space Complexity : O(N) - to create a new sorted linked list
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        v = []
        for l in range(n):
            while lists[l]:
                v.append(lists[l].val)
                lists[l] = lists[l].next
        v.sort()
        head = ListNode(0)
        t = head
        for node in v:
            t.next = ListNode(node)
            t = t.next
        return head.next