import unittest
from remove_k_from_list import show_list, removeKFromList, ListNode
from is_list_palindrome import is_list_palindrome
from merge_two_linked_lists import merge_two_linked_lists

class TestRemoveKFromList(unittest.TestCase):
    
    def test_value_in_list(self):
        l1 = ListNode(3)
        l1.next = ListNode(1)
        l1.next.next = ListNode(2)
        l1.next.next.next = ListNode(3)
        l1.next.next.next.next = ListNode(4)
        l1.next.next.next.next.next = ListNode(5)

        ll1 = removeKFromList(l1, 3)

        self.assertEqual(show_list(ll1), [1, 2, 4, 5])

    def test_value_not_in_list(self):
        l2 = ListNode(2)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)
        l2.next.next.next = ListNode(5)
        l2.next.next.next.next = ListNode(6)
        l2.next.next.next.next.next = ListNode(7)

        ll2 = removeKFromList(l2, 10)
        
        self.assertEqual(show_list(ll2), [2, 3, 4, 5, 6, 7])

class TestIsListPalindrome(unittest.TestCase):
    
    def test_it_is_palindrome(self):
        l1 = ListNode(0)
        l1.next = ListNode(1)
        l1.next.next = ListNode(0)

        self.assertEqual(is_list_palindrome(l1), True)

    def test_it_not_is_palindrome(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(2)
        l1.next.next.next = ListNode(3)

        self.assertEqual(is_list_palindrome(l1), False)

class TestMergeTwoLinkedLists(unittest.TestCase):

    def test_merge_first_case(self):
        l1 = ListNode(1)
        l1.next = ListNode(1)
        l1.next.next = ListNode(2)
        l1.next.next.next = ListNode(4)

        l2 = ListNode(0)
        l2.next = ListNode(3)
        l2.next.next = ListNode(5)

        merged_list = merge_two_linked_lists(l1=l1, l2=l2)

        self.assertEqual(show_list(merged_list), [0, 1, 1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()

# python -m unittest -v tests
