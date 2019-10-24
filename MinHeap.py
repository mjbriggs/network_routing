from NetworkHeap import NetworkHeap

class MinHeap(NetworkHeap):
    
    def __init__(self):
        self.queue = []
        self.dist_array = []
        self.prev_array = []
        self.pointers = []

    def makeQueue(self, graph, dist_array, prev_arr):
        self.dist_array = dist_array
        self.prev_array = prev_arr

        for n in range(len(graph)):
            self.queue.append(n)
            self.pointers.append(n)
        
        # print(self.queue)
        # print(self.pointers)
        # print(self.dist_array)
        # print(self.prev_array)


    def insert(self, node):
        self.bubbleUp(node)

    def deleteMin(self):
        self.printLists("deleteMin")

        if self.length() == 0:
            return -1
        else:
            x = self.queue[0]
            self.pointers[x] = -1
            node = self.queue[self.length() - 1]
            self.queue.pop(self.length() - 1)
            self.siftDown(node, 0) # takes bottom node and sticks it in the top
            return x

    def decreaseKey(self, node):
        self.printLists("decreaseKey(" + str(node) + ")")

        if self.length() != 0:
            print(node, " pointer value is ", self.pointers[node])            
            self.bubbleUp(node)

    def length(self):
        return len(self.queue)
    
    def updateDistance(self, index, distance):
        super().updateDistance(index, distance)
    
    def updatePrev(self, index, prev):
        super().updatePrev(index, prev)


    def bubbleUp(self, id):
        if self.length() <= 0: 
            return

        idPos = self.pointers[id]
        endPos = self.length() - 1
        end = self.queue[endPos]
        self.queue[idPos] = end 
        self.queue[endPos] = id
        self.pointers[end] = idPos
        self.pointers[id] = endPos

        position = self.pointers[id]

        self.printLists("bubbleUp")

        parent = self.parent(id, position)

        print("parent in bubbleUp is ", str(parent))
        while position > 0 and self.dist_array[parent] > self.dist_array[id]:
            parentPos = self.pointers[parent]
            self.queue[position] = parent
            self.queue[parentPos] = id
            self.pointers[parent] = position
            self.pointers[id] = parentPos
            position = parentPos
            parent = self.parent(id, position)
            self.printLists("parent is now " + str(self.queue[self.pointers[id]]) + " at position " + str(self.pointers[id]))


        self.queue[position] = id 
        self.pointers[id] = position

        self.printLists("end of bubbleUp")

        

    def siftDown(self, id, position):
        if self.length() <= 0: 
            return

        self.queue[position] = id
        self.pointers[id] = position
        child = self.minChild(id, position)

        self.printLists("siftDown")
        # print(child)

        print("child in siftDown is ", str(child))
        while child != -1 and self.dist_array[child] < self.dist_array[id]:
            childPos = self.pointers[child]
            self.queue[position] = child
            self.queue[childPos] = id
            self.pointers[child] = position
            self.pointers[id] = childPos
            print("child is now ", id)
            position = childPos
            child = self.minChild(id, position)
        
        self.queue[position] = id
        self.pointers[id] = position

        self.printLists("end of siftDown")
            

    def minChild(self, id, position): # returns the node_id of the minimum child
        # if 2*position >= self.length(): # means there are no children
        #     return -1
        # else:
        left = self.leftChild(id, position)
        right = self.rightChild(id, position)
        retVal = None

        if left < 0 and right < 0: # no children
            retVal = -1
        elif left < 0 and right >= 0: # no left child but right child
            retVal = right
        elif left >= 0 and right < 0: # no right child but left child
            retVal = left
        else:                         # two children
            if self.dist_array[left] < self.dist_array[right]:
                retVal = left
            else:   #for tiebreaker return right child
                retVal = right

        print("min child of ", id, " is ", retVal)
        return retVal

                    
    def leftChild(self, id, position):
        print(id, " ", position, " ", self.queue[position])
        self.printLists("leftChild")
        assert self.queue[position] == id
        leftPos = 2*position + 1
        if leftPos >= self.length():
            return -1
        else:
            return self.queue[leftPos]

    def rightChild(self, id, position):
        assert self.queue[position] == id
        rightPos = 2*position + 1
        if rightPos >= self.length():
            return -1
        else:
            return self.queue[rightPos]

    def parent(self, id, position):
        assert self.queue[position] == id
        parentPos = (position - 1) // 2
        if parentPos < 0:
            return -1
        else:
            return self.queue[parentPos]

    def printLists(self, location):
        print("in ", location)
        print("minHeap ", self.queue)
        print("pointers ", self.pointers)
        print("distances ", self.dist_array)
        print("prevs, ", self.prev_array)

        

