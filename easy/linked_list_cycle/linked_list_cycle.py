from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:

    '''Solution 1'''
    # dict = {}
    # while head:
    #     if dict.get(head):
    #         return True
        
    #     dict[head] = head.val
    #     head = head.next
    
    # return False

    '''Solution 2'''
    
    # Floyd's tortoise and hare algorithm, fast and slow pointer -> always O(n) time since distance between slow and    fast pointer is reduced by 1 in each iteration

    slow_pointer, fast_pointer = head, head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if(fast_pointer == slow_pointer):
            return True
    return False