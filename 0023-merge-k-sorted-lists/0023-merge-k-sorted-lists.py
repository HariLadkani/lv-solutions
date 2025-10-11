# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        head = ListNode()
        counter = 0
        for l in lists:
            if l:
                min_heap.append((l.val, counter, l.next))
                counter += 1

        heapq.heapify(min_heap)
        current = head
        while min_heap:
            value, _, next_node = heapq.heappop(min_heap)
            current.next = ListNode(val=value)
            if next_node:
                heapq.heappush(min_heap, (next_node.val, counter+1, next_node.next))
            current = current.next
            counter = counter + 1

        return head.next
