from dataclasses import dataclass, field

from vertex import Vertex
from edge import Edge

@dataclass
class Graph:

    name: str
    observation: str = "demo"

    _vertex_dict: dict[str, Vertex] = field(default_factory=dict[str, Vertex])
    _edge_dict: dict[str, Edge] = field(default_factory=dict[str, Edge])

    def add_vertex(self, vert: Vertex):
        self._vertex_dict[vert.id] = vert

    def add_edge(self, edge: Edge):
        v1: Vertex = self._vertex_dict[edge.inicial_id]
        v2: Vertex = self._vertex_dict[edge.final_id]
        v1.add_neighbor(v2.id)
        v2.add_neighbor(v1.id)
        self._edge_dict[edge.id] = edge

    def print_this(self):
        print(f"Graph: {self.name}")
        for id, vert in self._vertex_dict.items():
            print(vert)

        for id, edge in self._edge_dict.items():
            print(edge)

    def get_vertices(self) -> dict[str, Vertex]:
        return self._vertex_dict
    
    def get_edges(self) -> dict[str, Edge]:
        return self._edge_dict

    def reset_depth(self):
        for edge in self._edge_dict.values():
            edge.inicial_depth = 0.0
            edge.final_depth = 0.0

    def copy_me(self) -> 'Graph':
        new_graph = Graph(self.name)
        
        for vert in self._vertex_dict.values():
            new_graph.add_vertex(Vertex.from_str(str(vert)))
        for edge in self._edge_dict.values():
            new_graph.add_edge(Edge.from_str(str(edge)))

        return new_graph

    def get_total_weight(self) -> float:
        return sum(edge.weight for edge in self._edge_dict.values())

    def save_to_file(self, filepath: str):
        filepath = f"{filepath}/{self.name}.txt"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"{len(self._vertex_dict)} {len(self._edge_dict)}\n{self.observation}\n")

            for vert in self._vertex_dict.values():
                f.write(str(vert) + "\n")

            for edge in self._edge_dict.values():
                f.write(str(edge) + "\n")
    
    @staticmethod
    def load_from_file(filepath: str):
        import os

        file_name = os.path.basename(filepath)
        name = os.path.splitext(file_name)[0]
        gf = Graph(name)

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        qtd_vertex, qtd_edge = map(int, lines[0].strip().split())

        gf.observation = lines[1].strip() if len(lines) > 1 else "demo"
        
        for i in range(2, 2 + qtd_vertex):
            gf.add_vertex(Vertex.from_str(lines[i].strip()))

        for i in range(2 + qtd_vertex, 2 + qtd_vertex + qtd_edge):
            gf.add_edge(Edge.from_str(lines[i].strip()))

        return gf
    