import unittest
from two_lists import merge_two_lists, ListNode

class TestTwoSum(unittest.TestCase):
    def test_find_two_sum(self):
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list1.next.next = ListNode(4)
        list2 = ListNode(1)
        list2.next = ListNode(3)
        list2.next.next = ListNode(4)
        result = ListNode(1)
        result.next = ListNode(1)
        result.next.next = ListNode(2)
        result.next.next.next = ListNode(3)
        result.next.next.next.next = ListNode(4)
        result.next.next.next.next.next = ListNode(4)
        output = merge_two_lists(list1, list2)
        while result is not None:
            self.assertEqual(output.val, result.val)
            output = output.next
            result = result.next
    
if __name__ == '__main__':
    unittest.main()
    