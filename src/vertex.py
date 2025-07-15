from dataclasses import dataclass, field

@dataclass
class Vertex:

    id: str
    name: str
    x: float
    y: float
    elevation: float
    description: str = ""
    pontual_contribution: float = 0.0
    neighbors: list = field(default_factory=list)

    def add_neighbor(self, neighbor_id):
        if neighbor_id not in self.neighbors:
            self.neighbors.append(neighbor_id)

    def remove_neighbor(self, neighbor_id):
        if neighbor_id in self.neighbors:
            self.neighbors.remove(neighbor_id)

    @staticmethod
    def form_str(data: str):
        parts = data.split(";")

        _id = parts[0]
        name = parts[1]
        x = float(parts[2])
        y = float(parts[3])
        elev = float(parts[4])
        desc = parts[5]
        pont_cont = float(parts[6])
        neighbors = []
        for part in parts[6:]:
            neighbors.append(part)

        return Vertex(_id, name, x, y, elev, desc, pont_cont, neighbors)


    def to_dict(self) -> dict[str, any]:
        return {
            "id": self.id,
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "elevation": self.elevation,
            "pontual_contribution": self.pontual_contribution,
            "description": self.description,
            "neighbors": self.neighbors.copy(),
        }

    def __str__(self):
        #vertex = 01;PV 01;34.0;23.4;11.9;0.0;;id1;id2
        out: str = f"{self.id};{self.name};{self.x:.3f};{self.y:.3f};{self.elevation:.3f};{self.description}"
        for vet_id in self.neighbors:
            out += f";{vet_id}"
        return out
