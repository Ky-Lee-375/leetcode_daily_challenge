# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        counter = 0
        curr = head
        while (curr):
            counter += 1
            curr = curr.next
        
        from_front = counter - n
        curr2 = head
        if n == counter: 
            return head.next
        
        for i in range(from_front-1):
            curr2 = curr2.next
        curr2.next = curr2.next.next
        return head
            
        