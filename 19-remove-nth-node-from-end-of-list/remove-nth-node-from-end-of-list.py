# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        i = 1
        prv = None
        reverse = prev
        # print(prev)
        while reverse:
            if i == n:
                if prv == None:
                    prev = reverse.next
                    break
                else:
                    prv.next = reverse.next
                    break
            prv = reverse
            reverse = reverse.next
            i += 1

        # print(prev)
        res = None
        while prev:
            nxt = prev.next
            prev.next = res
            res = prev
            prev = nxt
        
        return res