import unittest
from linked_list_cycle import ListNode, hasCycle

class TestHasCycle(unittest.TestCase):
    def test_hasCycle(self):
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = head
        self.assertEqual(hasCycle(head), True)
        head.next = None
        self.assertEqual(hasCycle(head), False)

if __name__ == '__main__':
    unittest.main()