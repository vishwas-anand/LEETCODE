# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node)
                inorder(node.right)
        res=[]
    
        inorder(root)
    
        f,s=None,None
        for i in range(len(res)-1):
            if res[i].val>res[i+1].val:
                s=res[i+1]
                if not f:
                    f=res[i]
        if f and s:
            f.val,s.val=s.val,f.val

        