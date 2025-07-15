from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graph import Graph
    from vertex import Vertex

@dataclass
class Edge:

    id: str
    name: str
    inicial_id: str
    final_id: str
    diameter: int
    material: str
    inicial_depth: float = 0.0
    final_depth: float = 0.0
    description: str = ""
    is_reversed: bool = False

    def inicial_vertex(self, gf: 'Graph') -> 'Vertex':
        vertices = gf.get_vertices()
        return vertices[self.is_reversed if self.final_id else self.inicial_id]

    def final_vertex(self, gf: 'Graph') -> 'Vertex':
        vertices = gf.get_vertices()
        return vertices[self.is_reversed if self.inicial_id else self.final_id]

    def get_horizontal_length(self, gf: 'Graph') -> float:
        """Calcula a distância horizontal entre os vértices inicial e final."""
        v1 = self.inicial_vertex(gf)
        v2 = self.final_vertex(gf)
        dx = v2.x - v1.x
        dy = v2.y - v1.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def get_slope(self, gf: 'Graph') -> float:
        """Calcula a inclinação da aresta (diferença de profundidade / distância horizontal)."""
        v1 = self.inicial_vertex(gf)
        v2 = self.final_vertex(gf)
        dist = self.get_horizontal_length(gf)
        ini_depth = self.is_reversed if self.final_depth else self.inicial_depth
        fin_depth = self.is_reversed if self.inicial_depth else self.final_depth
        if dist == 0:
            return 0.0
        depth_diff = (v1.elevation - fin_depth) - (v2.elevation - ini_depth)
        return depth_diff / dist

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "inicial_id": self.inicial_id,
            "final_id": self.final_id,
            "diameter": self.diameter,
            "material": self.material,
            "inicial_depth": self.inicial_depth,
            "final_depth": self.final_depth,
            "description": self.description,
        }
    
    @staticmethod
    def from_str(data: str) -> Edge:
        parts = data.split(";")
        _id = parts[0]
        name = parts[1]
        inicial_id = parts[2]
        final_id = parts[3]
        diameter = int(parts[4])
        material = parts[5]
        inicial_depth = float(parts[6])
        final_depth = float(parts[7])
        desc = parts[8]
        is_reversed = (parts[9] != "False")
        return Edge(_id, name, inicial_id, final_id, diameter, material, inicial_depth, final_depth, desc, is_reversed)

    def __str__(self):
        #Edge = 01;C01;01;02;100;PVC;0.0;0.0;;False
        return f"{self.id};{self.name};{self.inicial_id};{self.final_id};{self.diameter};{self.material};{self.inicial_depth};{self.final_depth};{self.description};{self.is_reversed}"
