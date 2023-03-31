from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def print(self):
        current = self.head
        while current is not None:
            print(current.val, end='')
            current = current.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = LinkedList()
        sum = 0
        while l1 != None and l2 != None:
            sum += l1.val + l2.val
            result.add(sum%10)
            l1 = l1.next
            l2 = l2.next
            if sum >= 10:
                sum = 1
            else:
                sum = 0
        if l1 is not None or l2 is not None:
            rest = l1 if l1 is not None else l2
            while rest is not None:
                result.add((rest.val + sum)%10)
                if rest.val + sum >= 10:
                    sum = 1
                else:
                    sum = 0
                rest = rest.next
        if sum == 1:
            result.add(1)

        result.print()
        return result.head
    
l1 = LinkedList()
l2 = LinkedList()
valuesl1 = [2,4,3]
valuesl2 = [5,6,4]
for val in valuesl1:
    l1.add(val)
for val in valuesl2:
    l2.add(val)

# l1.print()
# l2.print()
s = Solution()
s.addTwoNumbers(l1.head, l2.head)
