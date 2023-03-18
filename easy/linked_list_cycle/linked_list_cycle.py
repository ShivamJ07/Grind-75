from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:

    '''Solution 1'''
    # Store all visited nodes in a dictionary, if current node exists in the dict, return true, else keep traversing until you reach last node
    # Time complexity is still O(n) but space complexity also ends up being O(n) at worst assuming all nodes are unique

    # dict = {}
    # while head:
    #     if dict.get(head):
    #         return True
        
    #     dict[head] = head.val
    #     head = head.next
    
    # return False

    '''Solution 2'''
    
    # Floyd's tortoise and hare algorithm, fast and slow pointer -> always O(n) time since distance between slow and fast pointer is reduced by 1 in each iteration
    # Fast pointer moves ahead by two nodes while slow pointer moves ahead by one node, if fast pointer catches up, there's a cycle, else not
    # If ever the next pointer of a node is None, it means the list ends and there is no cycle
    # Time complexity: O(n) - linear time complexity since distance between fast pointer and slow pointer is reduced by one node in each iteration, so time taken for fast pointer to catch up would be linearly proportional to length of list
    # Space complexity: O(1) - constant space use since we only declare a couple of variables
    slow_pointer, fast_pointer = head, head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if(fast_pointer == slow_pointer):
            return True
    return False