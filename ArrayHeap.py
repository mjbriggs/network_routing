from NetworkHeap import NetworkHeap

class ArrayHeap(NetworkHeap):

    def __init__(self):
        self.heap = []
        self.dist_array = []
        self.prev_array = []

    def makeQueue(self, graph, dist_array, prev_arr):
        print("makeQueue")
        self.dist_array = dist_array
        self.prev_array = prev_arr
        #uses dist_array indices as key values
        for i in range(len(graph)):
            self.heap.append(i)
        print("heap size is ", len(self.heap))
        print(self.heap)
        return self.heap

    def insert(self, node):
        print("insert")

    def deleteMin(self):
        #will return minimum node
        print("deleteMin")
        print("heap ", self.heap)
        print("dist_array, ", self.dist_array)
        print("prev_array ", self.prev_array)
        if len(self.heap) < 1:
            return -1
        # this just signals that we are at the start of the loop, 
        min_index = -1
        min = -1
        i = 0             
        while i < len(self.heap):
            if min_index < 1:
                min_index = self.heap[i]
                min = self.dist_array[min_index]
            print("i == ", i, " heap length is ", len(self.heap))
            print("at min_index ", min_index, " min distance is ", min)
            if min == 0:
                    print("at min_index ", min_index, " min distance is ", min)
                    self.heap.remove(min_index)
                    return min_index
            elif self.dist_array[self.heap[i]] == -1:
                print("distance value is -1")
            elif min == -1 and self.dist_array[self.heap[i]] > 0:
                print("setting new min at ", self.heap[i])
                min_index = self.heap[i]
                min = self.dist_array[min_index]
            elif min > self.dist_array[self.heap[i]]:
                print("setting new min at ", self.heap[i])
                min_index = self.heap[i]
                min = self.dist_array[min_index]
            i += 1

        # for i in range(len(self.heap)):
        #     if min_index == -5: # start of loop, set min_index and min to first element
               
        #     else:
                
        
        self.heap.remove(min_index)
        return min_index

    def decreaseKey(self, node):
        print("decreaseKey")

    def length(self):
        print("heap length is ", len(self.heap))
        return len(self.heap)