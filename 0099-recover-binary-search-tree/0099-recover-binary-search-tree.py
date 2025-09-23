# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1:
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

        

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node):
            curr=root
            while curr:
                if curr.left is None:
                    res.append(curr)
                    curr=curr.right
                else:
                    pred=curr.left
                    while pred.right and pred.right!=curr:
                        pred=pred.right
                    if pred.right is None:
                        pred.right=curr
                        curr=curr.left
                    else:
                        pred.right=None
                        res.append(curr)
                        curr=curr.right

        
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

        