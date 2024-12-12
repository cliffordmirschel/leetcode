# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        prev = None
        curr = head

        while curr:
            # save a ref to next node
            next_node = curr.next
            # set next node back to prev
            curr.next = prev
            # set prev node to curr
            prev = curr
            # Iterate curr forward
            curr = next_node
        
        return prev
