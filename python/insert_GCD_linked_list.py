import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        curr = head
        while curr.next:
            curr.next, curr = ListNode(math.gcd(curr.val, curr.next.val), curr.next), curr.next
        return head
        