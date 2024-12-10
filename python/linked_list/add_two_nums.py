"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""


# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        h1 = l1
        h2 = l2
        num_1 = []
        num_2 = []
        while h1:
            num_1.append(h1.val)
            h1 = h1.next
        
        while h2:
            num_2.append(h2.val)
            h2 = h2.next

        num = int(''.join(map(str,num_1[::-1]))) + int(''.join(map(str,num_2[::-1])))
        
        sum_arr = [int(x) for x in str(num)]
        print(sum_arr)
        if len(sum_arr):
            head = ListNode(sum_arr.pop())
        temp = head
        while len(sum_arr):
            temp.next = ListNode(sum_arr.pop())
            temp = temp.next
        
        return head

            
