# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        curr = fast = head
        while fast and fast.next:
            fast = fast.next.next
            curr = curr.next
            if curr == fast:
                return True
        return False