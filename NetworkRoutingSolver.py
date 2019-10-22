#!/usr/bin/python3


from CS312Graph import *
import time
import math
from NetworkHeap import NetworkHeap
from ArrayHeap import ArrayHeap


class NetworkRoutingSolver:
    def __init__( self ):                                                                                                               
        self.dist_arr = [] 
        self.prev_arr = []
        self.shortestPath = []
        self.savedPath = []
        self.visited = []

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def explore(self, srcIndex, destIndex):
        # print("exploring at node ", srcIndex, " looking for node ", destIndex)
        self.visited[srcIndex] = True
        self.shortestPath.append(srcIndex)
        # print("pushing ", srcIndex, " onto stack")
        if srcIndex == destIndex:
            # print("found destination node, path is ", self.shortestPath)
            self.savedPath = [i for i in self.shortestPath]
            return
        else:
            node = self.network.nodes[srcIndex]
            visits = 0
            # print("checking ", srcIndex, "'s children")
            for n in node.neighbors:
                # print("child is ", n.dest)
                # print("visited == ", self.visited[n.dest.node_id])
                # print("prev_array value is ", self.prev_array[n.dest.node_id], " and srcIndex is ", srcIndex)
                if self.visited[n.dest.node_id] == False and self.prev_array[n.dest.node_id] == srcIndex:
                    self.explore(n.dest.node_id, destIndex)
                    visits += 1
            
            # print("popping ", srcIndex, " off of stack")
            self.shortestPath.pop()

    def getShortestPath( self, destIndex ):
        self.dest = destIndex
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        path_edges = []
        total_length = 0
        path_nodes = []
        path_nodes.append(self.source)
        found_nodes = []
        current_node = self.source

        print("finding path to ", destIndex)
        self.explore(self.source, destIndex) 
        print("done")

        # print("network dist ", self.dist_array)
        # print("network prev ", self.prev_array)
        # print("path_nodes ", self.savedPath)

        next_nodes = []
        next_nodes.append(current_node)
        next_node = 0
        more_children = True
        # just trying to print entire shortest path tree
        showTree = False
        showPath = len(self.savedPath) > 0
        if showTree:
            while more_children:
                temp_next_nodes = []
                for n in range(len(next_nodes)):
                    current_node = next_nodes[n]
                    # print("current_node ", current_node)
                    found_nodes.append(current_node)
                    node = self.network.nodes[current_node]
                    # print("node = ", node)
                    for neighbor in range(3):
                        edge = node.neighbors[neighbor]
                        # print("edge = ", edge)
                        if self.prev_array[edge.dest.node_id] == current_node:
                            # print(edge.dest.node_id, " has a parent node ", current_node)
                            if not edge.dest.node_id in found_nodes:
                                # print("found next node ", edge.dest.node_id)
                                # print("found_nodes ", str(found_nodes))
                                path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
                                total_length += edge.length
                                temp_next_nodes.append(edge.dest.node_id)

                if len(temp_next_nodes) == 0:
                    more_children = False
                else:
                    next_nodes = temp_next_nodes
        elif showPath:
            print("showing path")
            savedPathLength = len(self.savedPath)
            # print("path length is ", savedPathLength)
            i = 0
            while i < savedPathLength:
                if i + 1 == savedPathLength:
                    break

                node = self.network.nodes[self.savedPath[i]]
                # print("at index ", i, " node is ", node)
                for e in node.neighbors:
                    if e.dest.node_id == self.savedPath[i + 1]:       
                        path_edges.append( (e.src.loc, e.dest.loc, '{:.0f}'.format(e.length)) )
                        total_length += e.length
                i += 1
        print("done")

        self.clearLists()

        return {'cost':total_length, 'path':path_edges}
    
    def clearLists(self):
        self.prev_array.clear()
        self.dist_array.clear()
        self.savedPath.clear()
        self.shortestPath.clear()
        self.visited.clear()

    def getEntireGraph(self):
        path_edges = []
        total_length = 0
        for node in self.network.getNodes():
            print(node)
            for e in node.neighbors:
                path_edges.append( (e.src.loc, e.dest.loc, str(e.src.node_id) + " " + '{:.0f}'.format(e.length) + " " + str(e.dest.node_id)) )
                total_length += e.length

        return {'cost':total_length, 'path':path_edges}


    def computeShortestPaths( self, srcIndex, use_heap=False ):
        print("computing path ...")
        self.source = srcIndex
        t1 = time.time()
        heap = None
        if not use_heap:
            heap = ArrayHeap()
        else:
            heap = ArrayHeap()
        
        for i in range(len(self.network.getNodes())):
            self.dist_arr.append(math.inf)
            self.prev_arr.append(math.inf)
            self.visited.append(False)

        self.dist_arr[self.source] = 0

        heap.makeQueue(self.network.getNodes(), self.dist_arr, self.prev_arr)
        nodes = self.network.getNodes()
        # for i in range(len(nodes)):
        #     print(nodes[i])
        #     print(nodes[i].neighbors)

        while heap.length() > 0:
            node_index = heap.deleteMin()
            # node = self.network.nodes[self.source]
            node = nodes[node_index]
            for e in range(len(node.neighbors)):
                neighbor_index = node.neighbors[e].dest.node_id
                neighbor_node = node.neighbors[e].dest
                edge = node.neighbors[e]
                # self.printDijkstraInfo(node_index, e, node, neighbor_index, neighbor_node, heap, edge)
                if heap.dist_array[neighbor_index] > heap.dist_array[node_index] + edge.length:
                    newDistance = heap.dist_array[node_index] + edge.length
                    heap.updateDistance(neighbor_index, newDistance)
                    heap.updatePrev(neighbor_index, node_index)
                    heap.decreaseKey(neighbor_index)
                
                    


        # print("array_heap dist ", array_heap.dist_array)
        # print("array_heap prev ", array_heap.prev_array)
        self.dist_array = heap.dist_array
        self.prev_array = heap.prev_array
                
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        t2 = time.time()
        print("done")
        return (t2-t1)

    def printDijkstraInfo(self, node_index, e, node, neighbor_index, neighbor_node, heap, edge):
        print("node_index ", node_index)
        print("node_edge_index, ", e)
        print("node ", node)
        print("neighbor_index ", neighbor_index)
        print("neighbor_node ", neighbor_node)
        print("neighbor dist value ", heap.dist_array[neighbor_index])
        print("edge ", edge)
        