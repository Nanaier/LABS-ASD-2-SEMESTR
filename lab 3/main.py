from networkx.generators.random_graphs import fast_gnp_random_graph
import random
import networkx as nx
import matplotlib.pyplot as plt
import pylab


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, start, end, weight):
        self.graph.append([start, end, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            start, end, weight = self.graph[i]
            i = i + 1
            x = self.find(parent, start)
            y = self.find(parent, end)
            if x != y:
                e = e + 1
                result.append([start, end, weight])
                self.apply_union(parent, rank, x, y)
        return result


def create_weighted_graph(n):
    p = 0.6
    w_edges = []
    l = [0, 0, 0]

    mode = int(input("Enter the mode: 1 - if you want random weights; 2 - if you want to input it yourself: "))

    gr = fast_gnp_random_graph(n, p)

    print("The list of all edges:", gr.edges)
    uw_edges = list(gr.edges())
    length = len(gr.edges)

    for i in range(0, length):
        l = [0, 0, 0]
        for j in range(0, 3):
            if j == 2:
                if mode == 1:
                    l[j] = random.randint(1, 7)
                if mode == 2:
                    l[j] = int(input("Enter the weight of the edge: "))
            else:
                l[j] = uw_edges[i][j]
        w_edges.append(l)

    return w_edges, length


def print_graph(w_edges, length, res):
    G = nx.Graph()
    for i in range(0, length):
        G.add_edges_from([(str(w_edges[i][0]), str(w_edges[i][1]))], weight = w_edges[i][2])

    edge_labels=dict([((u,v,),d['weight'])
                     for u,v,d in G.edges(data=True)])

    red_edges = []
    for i in range(0, len(res)):
        red_edges.append((str(res[i][0]), str(res[i][1])))

    edge_colors = ['r' if edge in red_edges else 'b' for edge in G.edges()]

    pos=nx.circular_layout(G)
    node_labels = {node:node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, node_color='blue', node_size=1200, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
    pylab.show()

def main():

    n = int(input("Enter the amount of nodes:"))
    g = Graph(n)

    w_edges, length = create_weighted_graph(n)

    for i in range(0, length):
        g.add_edge(w_edges[i][0], w_edges[i][1], w_edges[i][2])

    print("The minimal tree:\n")
    res = g.kruskal_algo()
    res_weight = 0
    res_len = len(res)
    for start, end, weight in res:
        res_weight += weight
        print("%d - %d: %d" % (start, end, weight))
    print('The weight of the tree:', res_weight)

    print_graph(w_edges, length, res)


if __name__ == '__main__':
    main()
