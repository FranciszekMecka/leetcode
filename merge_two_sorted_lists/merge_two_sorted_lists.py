from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        iter1 = list1
        iter2 = list2
        head = ListNode()
        while iter1 != None or iter2 != None:
            pass



head1: ListNode = ListNode(0, None)
head2: ListNode = ListNode(10, None)
iter1 = head1
iter2 = head2
for i in range(10):
    iter1.next = ListNode(i)
    iter1 = iter1.next
    iter2.next = ListNode(i + 10)
    iter2 = iter2.next

iter1 = head1
iter2 = head2
while iter1 is not None:
    print('iter1:', iter1.val)
    print('iter2:', iter2.val)

    iter1 = iter1.next
    iter2 = iter2.next