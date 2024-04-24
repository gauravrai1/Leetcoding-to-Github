# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Using fast and slow iterators to find the middle of the LL
        second = ListNode(0)
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None

        if not second:
            return

        # Reverse the second LL
        # rev_second = ListNode(val=second.val, next=None)
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        rev_second = prev

        # Merge the list
        while head.next and rev_second.next:
            nxt = head.next
            head.next = rev_second
            rev_second = rev_second.next
            head.next.next = nxt
            head = head.next.next
        
        if rev_second:
            if head.next:
                rev_second.next = head.next
            head.next = rev_second