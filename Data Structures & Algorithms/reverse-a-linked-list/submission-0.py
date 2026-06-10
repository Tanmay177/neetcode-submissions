# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if head == None:
            return None
        if curr.next == None:
            return curr
        next1 = curr.next
        curr.next = None
        print(curr.val,next1.val)
        while next1.next:
            next2 = next1.next
            #assign new link
            next1.next = curr
            #reassign
            curr = next1
            next1 = next2

        next1.next = curr
        curr = next1
        return curr



        