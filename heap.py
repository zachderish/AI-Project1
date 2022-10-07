
'''
This is a min heap
'''

def swap(list,a,b):
    list[a], list[b] = list[b], list[a]

class heap():
    def __init__(self):
        self.heap = []
        self.heap.append("don't touch the 0 index of a binary heap")

    def insert(self,item):
        size = len(self.heap)
        self.heap.append(item)
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
            elif index*2 < len(self.heap):
                if self.heap[index] > self.heap[index*2]:
                    swap(self.heap, index, index*2)
                    index = index*2
                    continue
            break
        
        return item

    def remove(self,item):
        '''
        throws expection if item not found
        else returns 0
        '''
        index = 0

        for i in range(1, len(self.heap)):
            if self.heap[i] == item:
                index = i
                break
        
        if index == 0:
            print("error: heap.remove, item to remove not found")
            return


        # Replace item with last item in heap, remove item, swim the replaced item to maintain order
        swap(self.heap,index,-1)
        self.heap.pop()

        # if item removed was the last item, skip rest
        if index == len(self.heap):
            return 0

        # Check swim down
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

        # Check swim up
        while index > 1:
            if self.heap[index] < self.heap[index//2]:
                swap(self.heap,index,index//2)
                index = index//2
                continue
            break
        
        return 0

    def contains(self,item):
        #self.listall()
        for i in self.heap[1:]:
            if i == item:
                return True
        return False

    def get_min(self):
        return self.heap[1]
    
    def get_size(self):
        return len(self.heap) - 1
    
    def listall(self):
        for i in range(len(self.heap)):
            print("index ", i, ": ", self.heap[i])
