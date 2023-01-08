# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# Example 1:


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy head 
        dummy = ListNode(0)
        dummy.next = head 
        cur = head 
        prev = dummy 
        while cur and cur.next : 
            first = cur
            second = cur.next
            prev.next = second 
            first.next = second.next 
            second.next = first

            # now it is prev-second-first-...
            prev = first
            cur = first.next

        return dummy.next # need to have dummy besides of prev to hold all values 
    
        return head
