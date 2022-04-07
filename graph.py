from vertex import Vertex
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.vertices: list[Vertex] = []

    def __iter__(self):
        return self.vertices

    def add_vertex(self, key):
        self.vertices.append(Vertex(key))

    def get_vertex(self, key: str):
        for vertex in self.vertices:
            if(vertex.key == key):
                return vertex
        return None

    def is_an_existing_vertex(self, vertex_src_key: str, vertex_dest_key: str):
        vortex = self.get_vertex(key)

    def add_edge(self, vertex_src: str, vertex_dest, weight=1):
        vertex_src = self.get_vertex(vertex_src)
        vertex_dest = self.get_vertex(vertex_dest) 
        vertex_src.add_point(vertex_dest.get_key(), weight)

    def show(self):
        text = 'Vertices: '
        for i in self.vertices:
            text += f'{i.get_key()} '
        text += '\nArestas:'
        for i in self.vertices:
            points = i.get_points()
            for point in points.keys():
                text += f'\n(src={i.get_key()}, dest={point}, weight={points[point]})'
        print(text)

    def plot(self):
        G = nx.Graph()
        
        for i in self.vertices:
            points = i.get_points()
            for point in points.keys():
                G.add_edge(i.get_key(), point, weight=points[point])
        
        pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
        
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)
        
        # edges
        nx.draw_networkx_edges(G, pos, width=6)
        
        # labels
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
        
        
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.savefig("teste.jpg")
        plt.clf()