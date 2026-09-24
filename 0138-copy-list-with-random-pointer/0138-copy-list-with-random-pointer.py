"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        
        can random point to itself?

        goal:
            return cloned copy of linkedlist

        approach:
            7: new 7
            13: new 13
            11: new 11
            10: new 10
            1: new 1
        original node: new node

        while none:

        hashmap[original].next = hashmap[original.next] 
        hashmap[original].random = hashmap[original.random] 
        '''
        if not head:
            return None

        hash_map = {}

        curr= head
        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            hash_map[curr].next = hash_map[curr.next] if curr.next else None
            hash_map[curr].random = hash_map[curr.random] if curr.random else None
            curr = curr.next

        return hash_map[head]
        
        