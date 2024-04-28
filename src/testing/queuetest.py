from src.datastructures import Queue
import unittest

class QueueTest(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue("test")
        q.enqueue(1.2)
        self.assertEqual(q.items, [1, "test", 1.2])

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue("test")
        q.enqueue(1.2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), "test")
        self.assertEqual(q.dequeue(), 1.2)

    def test_front_rear(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.front(), 1)
        self.assertEqual(q.rear(), 3)

    def test_size_empty(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())

if __name__ == '__main__':
    unittest.main()