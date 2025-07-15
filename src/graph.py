from __future__ import annotations
from dataclasses import dataclass, field

from vertex import Vertex
from edge import Edge

@dataclass
class Graph:

    name: str

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
        for id, vert in self._vertex_dict.items():
            print(vert)

        for id, edge in self._edge_dict.items():
            print(edge)

    def get_vertices(self) -> dict[str, Vertex]:
        return self._vertex_dict
    
    def get_edges(self) -> dict[str, Vertex]:
        return self._edge_dict
    
    def save_to_file(self, filepath: str):
        filepath = f"{filepath}/{self.name}.txt"
        with open(filepath, "w", encoding="utf-8") as f:
            # Escreve a primeira linha com as quantidades
            f.write(f"{len(self._vertex_dict)} {len(self._edge_dict)}\n")
            # Escreve os vértices
            for vert in self._vertex_dict.values():
                f.write(str(vert) + "\n")
            # Escreve as arestas
            for edge in self._edge_dict.values():
                f.write(str(edge) + "\n")

    @staticmethod
    def load_from_file(filepath: str) -> Graph:
        import os

        name = os.path.splitext(os.path.basename(filepath))[0]
        gf = Graph(name)

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        qtd_vertex, qtd_edge = map(int, lines[0].strip().split())

        for i in range(1, 1 + qtd_vertex):
            gf.add_vertex(Vertex.form_str(lines[i].strip()))

        for i in range(1 + qtd_vertex, 1 + qtd_vertex + qtd_edge):
            gf.add_edge(Edge.from_str(lines[i].strip()))

        return gf
    