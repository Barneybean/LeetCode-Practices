# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        # will not create a third linkedlist, this dymmy is only a node
        while list1 and list2: 
            
            if list1.val < list2.val:
                # make list1 the next of dummy and move on
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                # >= then make list2 the next 
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        # if 1 list end, the attache the remaining 
        cur.next = list1 if list1 else list2

        return dummy.next



