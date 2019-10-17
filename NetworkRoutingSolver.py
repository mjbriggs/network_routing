#!/usr/bin/python3


from CS312Graph import *
import time
from NetworkHeap import NetworkHeap
from ArrayHeap import ArrayHeap


class NetworkRoutingSolver:
    def __init__( self ):
        self.dist_arr = [] 
        self.prev_arr = []
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath( self, destIndex ):
        self.dest = destIndex
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        path_edges = []
        total_length = 0
        node = self.network.nodes[self.source]
        edges_left = 3
        while edges_left > 0:
            edge = node.neighbors[2]
            path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
            total_length += edge.length
            node = edge.dest
            edges_left -= 1
        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()
        array_heap = ArrayHeap()

        for i in range(len(self.network.getNodes())):
            self.dist_arr.append(-1)
            self.prev_arr.append(-1)

        self.dist_arr[self.source] = 0

        array_heap.makeQueue(self.network.getNodes(), self.dist_arr, self.prev_arr)
        
        while array_heap.length() > 0:
            node_index = array_heap.deleteMin()
            node = self.network.nodes[self.source]
            node = self.network.nodes[node_index]
            for e in range(len(node.neighbors)):
                print(node.neighbors[e])
                # if array_heap.dist_array[node_index] > array_heap.dist_array[edge]

        array_heap.decreaseKey(None)
        array_heap.deleteMin()
        # for i in range(self.source):

        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        t2 = time.time()
        return (t2-t1)

