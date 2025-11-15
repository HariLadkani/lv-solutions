# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Input: root of tree, node p, node q
        Goal:
            find lowest common ancestor of node p and q in tree root
        output:
            tree node that is lowest common ancestor

        constraint: 
            node p can be lowest common ancestor of node q or vice versa
            not a binary search tree
            p != q


        questions:
            min size of tree? 2 
            max size of tree? 10^5
            can p and q be same nodes? No
            are p and q in tree node? yes

        Two actions:
            find p and q in tree? Nops
            can we flatten in array? nops because it is not binary search tree

        approach:
            traverse up the tree from bottom up
            add to set at each node level
            then check if set has both p and q
            if lowest common ancestor, already assigned, return and break
            else lca should be none 
            run time: o(n)
            space: o(n)
        '''
        lca = None
        def dfs(currNode, p, q):
            if currNode == None:
                return set()

            nonlocal lca
            left_descendants = dfs(currNode.left, p, q)
            right_descendants = dfs(currNode.right, p, q)
            descendants = left_descendants.union(right_descendants)
            descendants.add(currNode)

            if p in descendants and q in descendants and lca == None:#we have not found lca before
                lca = currNode

            return descendants
        dfs(root, p, q)
        return lca

