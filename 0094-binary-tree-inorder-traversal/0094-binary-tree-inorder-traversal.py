# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder of O(1) which is in Morris Method
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        curr=root
        while curr:
            if curr.left is None:
                res.append(curr.val)
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
                    res.append(curr.val)
                    curr=curr.right
        return res
        