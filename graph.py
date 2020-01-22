from collections import deque, namedtuple

Edge = namedtuple("Edge", ["vertex", "weight"])

class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}
        self.vertices = set()
    
    @property
    def n_vertices(self):
        return len(self.adj_list)

    def add_vertex(self, v):
        self.adj_list[v] = set()
        self.vertices.add(v)
    
    def add_edge(self, source, dest, weight=1):
        try:
            self.adj_list[source].add(Edge(dest, weight))
            if not self.directed:
                self.adj_list[dest].add(Edge(source, weight))
        except KeyError:
            raise ValueError(f"{source} is not a vertex in the graph")
    
    def __getitem__(self, item):
        return self.adj_list[item]

    def __repr__(self):
        return f"Graph({set(self.adj_list.keys())})"
    
    def __str__(self):
        return f"Graph({set(self.adj_list.keys())})"

# BFS

def BFS(graph, start_node, process_func=print):
    visited = set()
    queue = deque([start_node])
    while queue:
        v = queue.popleft()
        if v not in visited:
            queue.extend([x.vertex for x in graph[v]]) #[0] is used to extract vertex fron (vertex, weight)
            process_func(v)
            visited.add(v)


def DFS(graph, start_node, process_func=print):
    visited = set()
    stack = [start_node]
    while stack:
        v = stack.pop()
        if v not in visited:
            stack.extend([n.vertex for n in graph[v]])
            process_func(v)
            visited.add(v)



def main():
    g = Graph() # https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_vertex(7)
    g.add_vertex(8)


    g.add_edge(0,1,4)
    g.add_edge(0,7,8)
    g.add_edge(1,7,11)
    g.add_edge(1,2,8)
    g.add_edge(7,8,7)
    g.add_edge(7,6,1)
    g.add_edge(2,8,2)
    g.add_edge(2,3,7)
    g.add_edge(2,5,4)
    g.add_edge(8,6,6)
    g.add_edge(6,5,2)
    g.add_edge(3,5,14)
    g.add_edge(3,4,9)
    g.add_edge(5,4,10)


    print("Breadth First Traversal")
    BFS(g, 0)
    print("Depth First Traversal")
    DFS(g, 0)

if __name__ == '__main__':
    main()