from __future__ import annotations
from dataclasses import dataclass, field

from vertex import Vertex
from edge import Edge

@dataclass
class Graph:

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