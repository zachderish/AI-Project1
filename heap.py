
import random

'''
This is a min heap
'''

def swap(list,a,b):
    list[a], list[b] = list[b], list[a]

class heap():
    def __init__(self) -> None:
        self.heap = []
        self.heap.append("don't touch the 0 index of a binary heap")

    def insert(self,object):
        size = len(self.heap)
        self.heap.append(object)
        while size > 1 and self.heap[size] < self.heap[size//2]:
            swap(self.heap,size,size//2)
            size = size//2
    
    def isEmpty(self):
        if len(self.heap) <= 1:
            return True
        return False
    
    def pop(self):
        # removes and returns the minimum
        if len(self.heap) < 2:
            return
        item = self.heap[1]
        swap(self.heap, 1, len(self.heap) - 1)
        self.heap.pop()
        #print('you popped')
        index = 1
        while True:
            if index*2 + 1 < len(self.heap):
                # check right and left
                right_is_min = True
                if self.heap[index*2 + 1] > self.heap[index*2]:
                    right_is_min = False
                if right_is_min:
                    if self.heap[index] > self.heap[index*2 + 1]:
                        swap(self.heap, index, index*2 + 1)
                        index = index*2 + 1
                        continue
                    else:
                        break
                else:
                    if self.heap[index] > self.heap[index*2]:
                        swap(self.heap, index, index*2)
                        index = index*2
                        continue
                    else: 
                        break
            if index*2 < len(self.heap):
                if self.heap[index] > self.heap[index*2]:
                    swap(self.heap, index, index*2)
                    index = index*2
                    continue
            break
        
        return item


    def get_min(self):
        return self.heap[1]
    
    def get_size(self):
        return len(self.heap) - 1
    

'''
testing
try inserting some stuff, the min heap is a binary tree where the parent is less than its children
'''
def main():
    test = heap()
    for i in range(10):
        test.insert(i)

    test.insert(3.2)
    test.insert(0.8)

    for j in range(len(test.heap)):
        print(test.heap[j])

    some = []
    item = test.pop()
    some.append(item)
    print('\n')
    for j in range(len(test.heap)):
        print(test.heap[j])


    j = test.pop()
    some.append(j)
    print('\n')

    for j in range(len(test.heap)):
        print(test.heap[j])

    for i in range(8):
        p = test.pop()
        some.append(p)

    print('\n')

    for a in some:
        print(a)
#main()

def main2():
    test = heap()
    for i in range(100):
        test.insert(random.randint(1,100000))
    
    a = []

    for i in range(test.get_size()):
        a.append(test.pop())

    for i in a:
        print(i)

main2()