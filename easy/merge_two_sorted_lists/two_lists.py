# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Time complexity: linear time - O(n) since time taken by program is proportional to size of lists
# Space complexity: constant space use - O(1) since we only create the dummy node, prehead and currhead pointers. 
    # we only reroute connections between exisitng nodes, not create new ones

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    # Create dummy node to keep reference to start of output list
    prehead = ListNode(-1)
    currhead = prehead

    # While neither list is none, keep comparing current values of both lists and append smaller value to output list
    while (list1 is not None and list2 is not None):
        if list1.val < list2.val:
            currhead.next = list1
            list1 = list1.next
        else:
            currhead.next = list2
            list2 = list2.next
        currhead = currhead.next

    # If either list is None, the rest of the output list must be the other list
    if list1 is None:
        currhead.next = list2
    if list2 is None:
        currhead.next = list1
    
    # Return next node of dummy node which is head of the output list
    return prehead.next

# Python assignment does not create new objects, it only creates new references to the same object
# Creating a dummy node is a useful way to maintain reference to a linked list whose actual contents are yet to be determined