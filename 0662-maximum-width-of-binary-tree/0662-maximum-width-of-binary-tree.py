# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Input: root of type TreeNode
        output: integer width
        goal:
            return MAX width of binary tree among all levels
            width of level = length between leftmost and rightmost non null nodes
            
                1
                
                1       2
            1    null 3   4
            
                [1,3,2,5,3,null,9]
                
                        1
                3               2
        5           3      null     9

                            1
                    3               2
            5         null   null       9    [5, null, null, 9]
        6                           7       null

        [5, null, null, 9]
        []
        [6, null,null, null, null, null, 7, null)
        '''
        if not root.left and not root.right:
            return 1

        deque = collections.deque([(root, 1)]) #[(node, index)]
        width = 1
        while deque:
            for i in range(len(deque)):
                node, index = deque.popleft()
                
                if node.left:
                    left_index = index * 2
                    deque.append((node.left, left_index))

                if node.right:
                    right_index = index * 2 + 1
                    deque.append((node.right, right_index))

            if len(deque) >= 2:
                width  = max(width,  deque[-1][1] - deque[0][1] + 1)
        return width


        