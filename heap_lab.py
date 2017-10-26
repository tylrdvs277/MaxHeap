# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Lab 7
# Term:        Fall 2017

class MaxHeap:

    def __init__(self, capacity = 50):
        self.heap_array = [0] * (capacity + 1)
        self.size = 0

    def insert(self, item):
        if self.size + 1 <= len(self.heap_array) - 1:
            self.heap_array[self.size + 1] = item
            self.size += 1
            self.perc_up(self.size)
            return True
        else:
            return False

    def find_max(self):
        return self.heap_array[1]

    def del_max(self):
        temp = self.heap_array[1]
        self.heap_array[1] = self.heap_array[self.size]
        self.heap_array[self.size] = 0
        self.size -= 1
        self.perc_down(1)
        return temp

    def heap_contents(self):
        return self.heap_array[1 : self.size + 1]

    def build_heap(self, alist):
        if len(alist) <= len(self.heap_array) - 1:
            self.heap_array[1 : len(alist) + 1] = alist
            self.size += len(alist)
            idx = self.size // 2
            while idx >= 1:
                self.perc_down(idx)
                idx -= 1
            return True
        else:
            return False

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size + 1 == len(self.heap_array)

    def get_heap_cap(self):
        return len(self.heap_array) - 1

    def get_heap_size(self):
        return self.size

    def perc_down(self, idx):
        done = False
        while idx * 2 <= self.size and not done:
            max_child_idx = self.max_child(idx)
            if self.heap_array[max_child_idx] > self.heap_array[idx]:
                temp = self.heap_array[idx] 
                self.heap_array[idx] = self.heap_array[max_child_idx]
                self.heap_array[max_child_idx] = temp
                idx = max_child_idx
            else:
                done = True

    def perc_up(self, idx):
        done = False
        while idx // 2 >= 1 and not done:
            parent_idx = idx // 2
            if self.heap_array[idx] > self.heap_array[parent_idx]:
                temp = self.heap_array[idx]
                self.heap_array[idx] = self.heap_array[parent_idx]
                self.heap_array[parent_idx] = temp
                idx = parent_idx
            else:
                done = True

    def max_child(self, idx):
        if idx * 2 + 1 <= self.size:
            if self.heap_array[idx * 2] > self.heap_array[idx * 2 + 1]:
                return idx * 2
            else:
                return idx * 2 + 1
        elif idx * 2 <= self.size:
            return idx * 2
        else:
            return None

    def heap_sort_increase(self, alist):
        self.build_heap(alist)
        max_idx = self.size
        while self.size > 0:    
            temp = self.heap_array[1]
            self.heap_array[1] = self.heap_array[self.size]
            self.heap_array[self.size] = temp
            self.size -= 1
            self.perc_down(1) 
        return self.heap_array[1 : max_idx + 1]
