# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        Input: TreeNode root, integer targetSum
        Ouput: Boolean
        Goal:
            return True if (sum of all node values from root to leaf) == targetSum
            return false otherwise

        constraint:
            0<=Tree.size <= 5000
            -1000<=node.val<=1000

        Questions:
            Should valid path have all the nodes from root to leef? yes
            min size of tree? 0
            max size of tree? 5000
            min value of node? -1000
            max value of node? 1000
            min value of sum? -1000 * 5000
            min value of targetSum? -1000
            max value of targetSum? 1000

        Edge case:
            tree.size = 0? False

        Approach:
            start at root 
            global flag = false
            if not root or global_flag == true:
                return
            current_sum += root.val
            if curren_sum ==  targetSum and not root.left and not root.right:
                global_flag = true

            dfs(root.left, current_sum)
            dfs(root.right, current_sum)

            run time: o(n)
            space: o(n)
        '''
        
        found = False

        def dfs(node, current_sum):
            nonlocal found
            if (not node) or found:
                return

            current_sum += node.val
            if current_sum == targetSum and (not node.left) and (not node.right):
                found = True
                return


            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

        dfs(root, 0)
        return found            

            