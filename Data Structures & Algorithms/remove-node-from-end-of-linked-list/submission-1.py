# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr1 = head
        curr2 = head
        final = head
        count = 0

        if head.next == None:
            return None
        while curr1.next != None:
            count += 1
            curr1 = curr1.next
        count += 1 #last node
        pos = count-n #4-2 =2
        if pos == 0:
            return curr2.next

        count1 = 0
        while curr2.next != None:
            count1 += 1
            if count1 == pos:
                next1 = curr2.next
                curr2.next = next1.next
                next1.next = None
                return final
            curr2 = curr2.next
        return final
