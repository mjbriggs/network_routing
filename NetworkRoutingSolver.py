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
        nodes = self.network.getNodes()
        print(nodes)
        while array_heap.length() > 0:
            node_index = array_heap.deleteMin()
            # node = self.network.nodes[self.source]
            node = nodes[node_index]
            for e in range(len(node.neighbors)):
                neighbor_index = node.neighbors[e].dest.node_id
                neighbor_node = node.neighbors[e].dest
                edge = node.neighbors[e]
                print("node_index ", node_index)
                print("node_edge_index, ", e)
                # print("node ", node)
                print("neighbor_index ", neighbor_index)
                # print("neighbor_node ", neighbor_node)
                # print("edge ", edge)
                if array_heap.dist_array[neighbor_index] > array_heap.dist_array[node_index] + edge.length:
                    print(array_heap.dist_array[neighbor_index], " > ", array_heap.dist_array[node_index], " + ", edge.length)
                    array_heap.dist_array[neighbor_index] = array_heap.dist_array[node_index] + edge.length
                    array_heap.prev_array[neighbor_index] = node_index
                    print(array_heap.dist_array)
                    print(array_heap.prev_array)
                elif(array_heap.dist_array[neighbor_index] < 0):
                    print(array_heap.dist_array[neighbor_index], " is now  ", array_heap.dist_array[node_index], " + ", edge.length)
                    array_heap.dist_array[neighbor_index] = array_heap.dist_array[node_index] + edge.length
                    array_heap.prev_array[neighbor_index] = node_index
                    print(array_heap.dist_array)
                    print(array_heap.prev_array)
                    


        print(array_heap.dist_array)
        print(array_heap.prev_array)
        array_heap.decreaseKey(None)
        array_heap.deleteMin()
        # for i in range(self.source):

        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        t2 = time.time()
        return (t2-t1)

