from dataclasses import dataclass

from config import LENGTH_FACTOR, DIAMETER_FACTOR, DEPTH_FACTOR

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
    weight: float = 0.0

    def inicial_vertex(self, vertices: dict[str, Vertex]) -> Vertex:
        return vertices[self.inicial_id]

    def final_vertex(self, vertices: dict[str, Vertex]) -> Vertex:
        return vertices[self.final_id]

    def get_horizontal_length(self, vertices: dict[str, Vertex]) -> float:
        """Calcula a distância horizontal entre os vértices inicial e final."""
        v1 = self.inicial_vertex(vertices)
        v2 = self.final_vertex(vertices)
        dx = v2.x - v1.x
        dy = v2.y - v1.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def get_slope(self, vertices: dict[str, Vertex]) -> float:
        """Calcula a inclinação da aresta (diferença de profundidade / distância horizontal)."""
        v1 = self.inicial_vertex(vertices)
        v2 = self.final_vertex(vertices)
        dist = self.get_horizontal_length(vertices)
        if dist == 0:
            return 0.0
        depth_diff = (v1.elevation - self.inicial_depth) - (v2.elevation - self.final_depth)
        return depth_diff / dist
    
    def update_weight(self, vertices: dict[str, Vertex]):
        length = self.get_horizontal_length(vertices)
        mid_depth = (self.inicial_depth + self.final_depth) / 2.0
        self.weight = LENGTH_FACTOR * length
        self.weight += DIAMETER_FACTOR * self.diameter
        self.weight += DEPTH_FACTOR * mid_depth * length

    def reverse(self):
        aux_id: str = self.inicial_id
        self.inicial_id = self.final_id
        self.final_id = aux_id

        aux_depth: float = self.inicial_depth
        self.inicial_depth = self.final_depth
        self.inicial_depth = aux_depth

    def is_adjacent(self, e2: 'Edge'):
        if self.inicial_id == e2.inicial_id: return True
        if self.inicial_id == e2.final_id: return True
        if self.final_id == e2.inicial_id: return True
        if self.final_id == e2.final_id: return True
        return False

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
    def from_str(data: str):
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
        return Edge(_id, name, inicial_id, final_id, diameter, material, inicial_depth, final_depth, desc)

    def __str__(self):
        #Edge = 01;C01;01;02;100;PVC;0.0;0.0;;False
        return f"{self.id};{self.name};{self.inicial_id};{self.final_id};{self.diameter};{self.material};{self.inicial_depth:.3f};{self.final_depth:.3f};{self.description}"
