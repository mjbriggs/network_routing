#!/usr/bin/python3


from CS312Graph import *
import time
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
                if self.visited[n.dest.node_id] == False and self.prev_array[n.dest.node_id] == srcIndex:
                    self.explore(n.dest.node_id, destIndex)
                    visits += 1
            
            #if visits == 0:
            # print("popping ", srcIndex, " off of stack")
            self.shortestPath.pop()

    def getShortestPath( self, destIndex ):
        self.dest = destIndex
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        path_edges = []

        i = 0
        current_node = self.source
        potential_node_index = 0
        next_indexes = []
        found_dest = False
        path_exists = True
        # while not found_dest and path_exists:
        #     for j in range(len(self.prev_array)):
        #         if(self.prev_array[j] == current_node):
        #             next_indexes.append(j)

        total_length = 0
        node = self.network.nodes[self.source]
        edges_left = 3
        index = 2
        # while edges_left > 0:
        #     # if prev_array.contains(node.neighbors[index]):
        #     edge = node.neighbors[2]
        #     path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
        #     total_length += edge.length
        #     node = edge.dest
        #     edges_left -= 1
        
        path_nodes = []
        path_nodes.append(self.source)
        found_nodes = []
        current_node = self.source
        max_edge = 3
        child = 0
        looping = True
        self.explore(self.source, destIndex) 

        print("network dist ", self.dist_array)
        print("network prev ", self.prev_array)
        print("path_nodes ", self.savedPath)

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
            print("path length is ", savedPathLength)
            i = 0
            while i < savedPathLength:
                if i + 1 == savedPathLength:
                    break

                node = self.network.nodes[self.savedPath[i]]
                print("at index ", i, " node is ", node)
                for e in node.neighbors:
                    if e.dest.node_id == self.savedPath[i + 1]:       
                        path_edges.append( (e.src.loc, e.dest.loc, '{:.0f}'.format(e.length)) )
                        total_length += e.length
                i += 1

        # edges_left = len(path_nodes)
        # while edges_left > 0:
        #     # if prev_array.contains(node.neighbors[index]):
        #     edge = node.neighbors[2]
        #     path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
        #     total_length += edge.length
        #     node = edge.dest
        #     edges_left -= 1
        self.prev_array.clear()
        self.dist_array.clear()
        self.savedPath.clear()
        self.shortestPath.clear()
        self.visited.clear()
        return {'cost':total_length, 'path':path_edges}
    
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
        self.source = srcIndex
        t1 = time.time()
        array_heap = ArrayHeap()
        
        for i in range(len(self.network.getNodes())):
            self.dist_arr.append(-1)
            self.prev_arr.append(-1)
            self.visited.append(False)

        self.dist_arr[self.source] = 0

        array_heap.makeQueue(self.network.getNodes(), self.dist_arr, self.prev_arr)
        nodes = self.network.getNodes()
        for i in range(len(nodes)):
            print(nodes[i])
            print(nodes[i].neighbors)

        while array_heap.length() > 0:
            node_index = array_heap.deleteMin()
            # node = self.network.nodes[self.source]
            node = nodes[node_index]
            for e in range(len(node.neighbors)):
                neighbor_index = node.neighbors[e].dest.node_id
                neighbor_node = node.neighbors[e].dest
                edge = node.neighbors[e]
                # print("node_index ", node_index)
                # print("node_edge_index, ", e)
                # print("node ", node)
                # print("neighbor_index ", neighbor_index)
                # print("neighbor_node ", neighbor_node)
                # print("edge ", edge)
                if array_heap.dist_array[neighbor_index] > array_heap.dist_array[node_index] + edge.length:
                    # print(array_heap.dist_array[neighbor_index], " > ", array_heap.dist_array[node_index], " + ", edge.length)
                    array_heap.dist_array[neighbor_index] = array_heap.dist_array[node_index] + edge.length
                    array_heap.prev_array[neighbor_index] = node_index
                    # print(array_heap.dist_array)
                    # print(array_heap.prev_array)
                elif(array_heap.dist_array[neighbor_index] < 0):
                    # print(array_heap.dist_array[neighbor_index], " is now  ", array_heap.dist_array[node_index], " + ", edge.length)
                    array_heap.dist_array[neighbor_index] = array_heap.dist_array[node_index] + edge.length
                    array_heap.prev_array[neighbor_index] = node_index
                    # print(array_heap.dist_array)
                    # print(array_heap.prev_array)
                    


        # print("array_heap dist ", array_heap.dist_array)
        # print("array_heap prev ", array_heap.prev_array)
        self.dist_array = array_heap.dist_array
        self.prev_array = array_heap.prev_array
        
        # for i in range(self.source):
        
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)
        t2 = time.time()
        return (t2-t1)

