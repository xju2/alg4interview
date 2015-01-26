#!/usr/bin/env python
class MinHeap:
    def __init__(self):
        print "A minimum heap is created!"
        self.array = [0]
        self.size = 0
       
        
    def insert(self, value):
        print str(value)+" is added!"
        self.array.append(value)
        self.size += 1
        self.percolateUp(self.size)


    def percolateUp(self,hole):
        value = self.array[hole]
        while value < self.array[hole/2] and hole > 1:
            self.array[hole] = self.array[hole/2]
            hole /=  2
        
        self.array[hole] = value

    def del_min(self):
        if self.size < 1:
            return None

        min_value = self.array[1]
        #print "min value: "+ str(min_value)
        self.array[1] = self.array[self.size]
        self.size -= 1
        self.percolateDown(1)
        return min_value

    def percolateDown(self,hole):
        value = self.array[hole]
        while 2*hole < self.size :
            child = 2*hole
            if self.array[child+1] < self.array[child]:
                child += 1

            if value > self.array[child]:
                self.array[hole] = self.array[child]
            else:
                break
                
            hole = child 

        self.array[hole] = value
        
    def decrease_key(self, p, delta):
        if p > self.size:
            print str(p)+" is out of size."
            return None
        if delta < 0:
            print "don't fool me with negative value: "+str(delta)
            return None
        print str(self.array[p])+" decrease to ",
        self.array[p] -= delta
        print str(self.array[p])
        up_p = self.array[p]
        self.percolateUp(p)
        return up_p

    def increase_key(self, p, delta):
        if p > self.size:
            print str(p)+" is out of size."
            return None
        if delta < 0:
            print "don't fool me with negative value: "+str(delta)
            return None
        
        print str(self.array[p])+" increase to ",
        self.array[p] += delta
        print str(self.array[p])
        update_p = self.array[p]
        self.percolateDown(p)
        return update_p
        

heap = MinHeap()
heap.insert(20)
heap.insert(10)
heap.insert(30)
heap.insert(12)
heap.insert(24)
heap.insert(121)
heap.insert(31)
heap.insert(133)

print "min: "+ str(heap.del_min())
print heap.decrease_key(3, 39)
print "min: "+ str(heap.del_min())
print heap.increase_key(1,10)
print "min: "+ str(heap.del_min())

