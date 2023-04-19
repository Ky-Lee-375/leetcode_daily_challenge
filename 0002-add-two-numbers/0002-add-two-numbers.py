# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(n:Optional[ListNode]):
            head1=n
            num=0
            i=0
            while head1 is not None:
                num += head1.val* (10 **i)
                i+=1
                head1=head1.next
            return num
     
    
        x = reverse(l1) + reverse(l2)
        curr = ListNode(x % 10, None)
        head = curr
        while x:
            x = x// 10
            if x != 0:
                curr.next = ListNode(x % 10, None)
                curr = curr.next
            else:
                return head
        else:
            return head
        