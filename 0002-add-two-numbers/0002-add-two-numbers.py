# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        goal:
            add two numbers and return sum as a linked list

        Constaints:
            digits are single digit(0-9)
            digits are in reverse order
            no leading zeroes except number 0
            l1.size may not be equal to l2.size

        2 -  4 - 3
        5 -  6 - 9

        7 - 0 - 8

        10 % 10 = 0
        10//10  = 1

        questions?
            min size of l1 and l2? 1 to 100
            node.val? 0 to 9

        Approach:
            iterate over two linkedlist 
                iterate max(l2.size, l1.size)

                add two nodes + carry
                compute remainder with sum%10 and divisor with sum//10
                newNode = remainder
                carry = divisor

            If carry, create a new node and add carry as value
            return head of list


            run time = o(len(l1), len(l2))
            space = o(max(l1.size, l2.size))   
        '''

        dummy = ListNode()
        curr = dummy   
        carry = 0 
        
        while l1 or l2 or carry!=0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            summation = l1_val + l2_val + carry
            remainder = summation % 10
            carry = summation // 10

            newNode = ListNode(remainder, None)
            curr.next = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return dummy.next

        