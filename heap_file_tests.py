# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 7
# Term:        Fall 2017

import unittest
import heap_lab

class TestLab7(unittest.TestCase):


    def test_insert(self):
        heap = heap_lab.MaxHeap(3)
        for i in range(1, 4):
            heap.insert(i)
        self.assertEqual(heap.heap_contents(), [3, 1, 2])

    def test_insert_full(self):
        heap = heap_lab.MaxHeap(3)
        for i in range(1, 4):
            heap.insert(i)
        self.assertFalse(heap.insert(4))

    def test_find_max(self):
        heap = heap_lab.MaxHeap(3)
        for i in range(1, 4):
            heap.insert(i)
        self.assertEqual(heap.find_max(), 3)

    def test_del_max(self):
        heap = heap_lab.MaxHeap(4)
        for i in range(1, 5):
            heap.insert(i)
        heap.del_max()
        self.assertEqual(heap.heap_contents(), [3, 1, 2])

    def test_heap_contents(self):
        heap = heap_lab.MaxHeap(4)
        for i in range(1, 5):
            heap.insert(i)
        self.assertEqual(heap.heap_contents(), [4, 3, 2, 1])

    def test_build_heap(self):
        heap = heap_lab.MaxHeap()
        heap.build_heap([9, 12, 15, 8, 16, 20])
        self.assertEqual(heap.heap_contents(), [20, 16, 15, 8, 12, 9])

    def test_is_empty(self):
        heap = heap_lab.MaxHeap()
        self.assertTrue(heap.is_empty())
        heap.insert(10)
        self.assertFalse(heap.is_empty())

    def test_is_full(self):
        heap = heap_lab.MaxHeap(3)
        self.assertFalse(heap.is_full())
        for i in range(1, 4):
            heap.insert(i)  
        self.assertTrue(heap.is_full())

    def test_get_heap_cap(self):
        heap = heap_lab.MaxHeap(3)
        self.assertEqual(heap.get_heap_cap(), 3)
    
    def test_get_heap_size(self):
        heap = heap_lab.MaxHeap(3)
        for i in range(1, 4):
            heap.insert(i)
            self.assertEqual(heap.get_heap_size(), i)

    def test_heap_sort_increase(self):
        mylist = [9, 12, 15, 8, 16, 20]
        heap = heap_lab.MaxHeap(len(mylist))
        self.assertEqual(heap.heap_sort_increase(mylist), [8, 9, 12, 15, 16, 20])

    
if __name__ == "__main__":
    unittest.main()

