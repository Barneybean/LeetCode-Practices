# Given the head of a singly linked list, reverse the list, and return the reversed list.
# 1->2->3
# out: 3->2->1

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Iterative Solution - T.C - O(n) , S.P - O(1)
        # add 1 to 2.next so the new link is 2-1
        # add 2 to 3.next so the new link is 3-2-1
        # repeat until end of the linked list (while)
        cur = head
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur 
            cur = next

        return prev
        
        # Recursive Solution - T.C - O(n) , S.P - O(n)
        # def reverseList(self, head: ListNode, prev=None) -> ListNode:
		# if head is None or head.next is None:
        #     return head
        # smallHead = self.reverseList(head.next)
        # tail = head.next
        # tail.next = head
        # head.next = None
        # return smallHead

