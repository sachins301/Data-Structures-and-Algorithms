import unittest

from src.datastructures import DoubleLinkedList


class MyTestCase(unittest.TestCase):
    def test_init(self):
        dll = DoubleLinkedList()
        self.assertEqual(dll.head, None)  # add assertion here

    def test_insert0(self):
        dll = DoubleLinkedList()
        dll.insert(10, 0)
        # print(linkedlist)
        self.assertEqual(10, dll.head.data)

    def test_insert1(self):
        dll = DoubleLinkedList()
        dll.insert(10,0)
        dll.insert(11, 1)
        print(dll)
        self.assertEqual(11, dll.head.next.data)

    def test_insert2(self):
        dll = DoubleLinkedList()
        dll.insert(10,0)
        dll.insert(11, 1)
        dll.insert(12, 2)
        self.assertEqual(11, dll.head.next.next.prev.data)

    def test_delete0(self):
        dll = DoubleLinkedList()
        dll.insert(10,0)
        dll.insert(11, 1)
        dll.delete(0)
        self.assertEqual(11, dll.head.data)

    def test_delete1(self):
        dll = DoubleLinkedList()
        dll.insert(10, 0)
        dll.insert(11, 1)
        dll.delete(1)
        print(dll)
        self.assertEqual(None, dll.head.next)


if __name__ == '__main__':
    unittest.main()
