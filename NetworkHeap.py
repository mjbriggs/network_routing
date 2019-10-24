import abc

# Abstract class that defines necessary behavior for network heaps
class NetworkHeap(abc.ABC):
    
    @abc.abstractmethod
    def makeQueue(self, graph, dist_array, prev_arr):
        pass

    @abc.abstractmethod
    def insert(self, node):
        pass

    @abc.abstractmethod
    def deleteMin(self):
        #will return minimum node
        pass

    @abc.abstractmethod
    def decreaseKey(self, node):
        pass

    @abc.abstractmethod
    def length(self):
        pass
    
    @abc.abstractmethod
    def updateDistance(self, index, distance):
        self.dist_array[index] = distance
    
    @abc.abstractmethod
    def updatePrev(self, index, prev):
        self.prev_array[index] = prev

