# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_x=ListNode(0)
        right_x=ListNode(0)
        left_head=left_x
        right_head=right_x
        while head:
            if head.val<x:
                left_x.next=ListNode(head.val)
                left_x=left_x.next
            else:
                right_x.next=ListNode(head.val)
                right_x=right_x.next
            head=head.next
        left_x.next=right_head.next
        return left_head.next        