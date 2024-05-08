from src.datastructures import LinkedList
import unittest


class MyTestCase(unittest.TestCase):
    def test_init(self):
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.head, None)  # add assertion here

    def test_insert0(self):
        linkedlist = LinkedList()
        linkedlist.insert(10, 0)
        # print(linkedlist)
        self.assertEqual(10, linkedlist.head.data)

    def test_insert1(self):
        ll = LinkedList()
        ll.insert(10,0)
        ll.insert(11, 1)
        print(ll)
        self.assertEqual(11, ll.head.next.data)

    def test_insert2(self):
        ll = LinkedList()
        ll.insert(10,0)
        ll.insert(11, 1)
        ll.insert(12, 2)
        self.assertEqual(12, ll.head.next.next.data)

    def test_delete0(self):
        ll = LinkedList()
        ll.insert(10,0)
        ll.insert(11, 1)
        ll.delete(0)
        self.assertEqual(11, ll.head.data)

    def test_delete1(self):
        ll = LinkedList()
        ll.insert(10, 0)
        ll.insert(11, 1)
        ll.delete(1)
        print(ll)
        self.assertEqual(None, ll.head.next)

if __name__ == '__main__':
    unittest.main()
