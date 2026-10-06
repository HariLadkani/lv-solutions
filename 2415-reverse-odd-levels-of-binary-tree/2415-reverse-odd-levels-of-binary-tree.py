# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


''''
left_node = current.left
left_left_child = left_node.left
left_right_child = left_node.right

right_node = current.right
right_left_node = right_node.left
right_right_node = right_node.right

left_node.left = right_left_node
left_node.right = right_right_node

........same for right

current.left = right_node
current.right = left_node

'''
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        '''
        queue 
        deque([TreeNode{val: 3, left: TreeNode{val: 8, left: None, right: None}, right: TreeNode{val: 13, left: None, right: None}}, TreeNode{val: 5, left: TreeNode{val: 21, left: None, right: None}, right: TreeNode{val: 34, left: None, right: None}}])


        '''

        level = 0
        queue = deque([root])
        while queue:
            if level % 2 != 0: #
                left = 0
                right = len(queue)-1

                while left < right:
             
                    left_value, right_value = queue[left].val, queue[right].val
                    queue[left].val, queue[right].val = right_value, left_value
                    left += 1
                    right -= 1

            for i in range(len(queue)):
                current_node = queue.popleft()
                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            level += 1

        return root