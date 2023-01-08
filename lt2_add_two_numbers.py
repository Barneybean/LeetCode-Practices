# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0 
        # carry will add 1 to next node if over 10 
        while l1 or l2 or carry!=0: # need carry != 0
            # if node is None then no .val
            l1_val = l1.val if l1 else 0 
            l2_val = l2.val if l2 else 0
            colsum = l1_val + l2_val + carry # carry 1
            carry = colsum // 10
            new_node = ListNode(colsum%10)
            cur.next = new_node
            cur = new_node # move to next 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next