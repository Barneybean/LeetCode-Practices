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
        # # create a dummy head to return dummy.next as new head of result 

        # dummy (prev) -> head (cur/first) ->  head.next(cur.next/second)->
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        
        # option 1
        # while cur and cur.next:
        #     first = cur # hold as temp
        #     second = cur.next # hold as temp
        #     prev.next = second # connect prev to second 
        #     first.next = second.next # connect first to jump over second
        #     prev.next.next = first # now it is prev -> second -> first -> originalsecond.next

        #     prev = first # now the first not cur
        #     cur = prev.next

        # option 2
        while cur and cur.next:
            prev.next = cur.next # connect prev to second 
            cur.next = cur.next.next # connect first to jump over second
            prev.next.next = cur # now it is prev -> second -> first -> originalsecond.next
            # print(cur)
            # print()
            # print(prev)
            prev = prev.next.next # jump two node after, last node of the previous swap
            # or prev = cur
            cur = prev.next # cur needs to be the first node to swap

        return dummy.next
        