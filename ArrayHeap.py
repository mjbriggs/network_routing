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
        min_index = -5
        min = -1

        for i in range(len(self.heap)):
            if min_index == -5:
                min_index = self.heap[i]
                min = self.dist_array[min_index]
            else:
                if min == 0:
                    print("at min_index ", min_index, " min distance is ", min)
                    self.heap.remove(min_index)
                    return min_index
                if min > self.dist_array[i]:
                    min_index = self.heap[i]
                    min = self.dist_array[min_index]
            print("at min_index ", min_index, " min distance is ", min)
        
        self.heap.remove(min_index)
        return min_index

    def decreaseKey(self, node):
        print("decreaseKey")

    def length(self):
        print(len(self.heap))
        return len(self.heap)