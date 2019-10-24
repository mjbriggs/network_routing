from NetworkHeap import NetworkHeap

class ArrayHeap(NetworkHeap):

    def __init__(self):
        self.queue = []
        self.dist_array = []
        self.prev_array = []

    def makeQueue(self, graph, dist_array, prev_arr):
        # print("makeQueue")
        self.dist_array = dist_array
        self.prev_array = prev_arr
        #uses dist_array indices as key values
        for i in range(len(graph)):
            self.insert(i)
        return self.queue

    def insert(self, node):
        # print("insert")
        self.queue.append(node)

    def deleteMin(self):
        #will return minimum node
        if len(self.queue) < 1:
            return -1
        min_index = self.queue[0]
        min = self.dist_array[min_index]
        i = 0             
        while i < len(self.queue):
            if min > self.dist_array[self.queue[i]]:
                # print("setting new min at ", self.heap[i])
                min_index = self.queue[i]
                min = self.dist_array[min_index]
            i += 1

        self.queue.remove(min_index)
        return min_index

    def decreaseKey(self, node):
        pass

    def length(self):
        return len(self.queue)

    def updateDistance(self, index, distance):
        super().updateDistance(index, distance)
    
    def updatePrev(self, index, prev):
        super().updatePrev(index, prev)