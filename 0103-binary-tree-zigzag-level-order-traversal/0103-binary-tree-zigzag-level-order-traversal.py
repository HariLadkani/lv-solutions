# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        '''
        BFS with depth level
        if depth level is even, keep order same as bfs from left to right
        if depth level is odd, add all the values in list and then reverse list
        increment depth level at eeach iteration

        '''
        if not root:
            return []

        res = []
        queue = deque([root])
        level = 0
        while queue:
            level_list = []
            for i in range(len(queue)):
                current = queue.popleft()
                level_list.append(current.val)
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            if len(level_list) > 0 and level % 2 != 0:
                level_list.reverse()
            res.append(level_list)
            level += 1

        return res

