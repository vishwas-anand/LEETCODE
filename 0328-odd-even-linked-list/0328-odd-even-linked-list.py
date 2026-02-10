# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=head
        eve=head.next
        ev_st=eve
        while eve and eve.next:
            odd.next=odd.next.next
            odd=odd.next
            eve.next=eve.next.next
            eve=eve.next
        odd.next=ev_st
        return head
        