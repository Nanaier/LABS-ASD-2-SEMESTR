from collections import defaultdict
import numpy as np
from random import *
class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size


    def add_edge(self, v1, v2, weight):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = weight


    def __len__(self):
        return self.size

    def print_matrix(self, n):
        for i in range(0, n):
            for j in range(0, n):
                if self.adjMatrix[i][j] == 0 and i!=j:
                    print('{:3}'.format('inf'), end = " ")
                else:
                    print('{:3}'.format(self.adjMatrix[i][j]), end=" ")
            print()



def input_amount():
    PROBABILITY = 70
    n = int(input("enter the amount of nodes in your graph:"))
    g = Graph(n)

    mode = input("choose the mode of filling up the matrix\n0 - for hand input\n1 - for random input\nenter mode:")
    if mode == '0':
        print("enter input data in format: <1 node> <2 node> <weight>\nto end input enter '<' in new line\n")
        for i in range(0, n*n):
            line = input()
            if (line[0]) == '<':
                break
            else:
                l = line.split()
                g.add_edge(int(l[0]), int(l[1]), int(l[2]))
    if mode == "1":
        limits_line = input("enter your limits range in one line <1 limit> <2 limit>:")
        limits = limits_line.split()
        for i in range(0, n):
            for j in range(i+1, n):
                if randrange(1, 100, 1) > PROBABILITY:
                    g.add_edge(i, j, randrange(int(limits[0]), int(limits[1]), 1))
                else:
                    g.add_edge(i, j, 0)
                if randrange(1, 100, 1) > PROBABILITY:
                    g.add_edge(j, i, randrange(int(limits[0]), int(limits[1]), 1))
                else:
                    g.add_edge(j, i, 0)
    print("matrix of weights:")
    g.print_matrix(n)

    algorithm = Algo(g.adjMatrix)
    source = 0
    sink = n-1

    print("Max Flow: %d " % algorithm.ford_fulkerson(source, sink))

class Algo:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)

    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False


    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


if __name__ == '__main__':
    input_amount()


