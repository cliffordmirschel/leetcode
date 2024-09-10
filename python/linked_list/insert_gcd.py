class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math
class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            new_val = math.gcd(node.val,node.next.val)
            temp = node.next
            node.next = ListNode(new_val, temp)
            node = temp
        return head