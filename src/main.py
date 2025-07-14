from vertex import Vertex
from edge import Edge
from graph import Graph

if __name__ == "__main__":
    gf = Graph()
    
    gf.add_vertex(Vertex(id="01", name="PV 01", x=34.0, y=23.4, elevation=11.9))
    gf.add_vertex(Vertex(id="02", name="PV 02", x=24.0, y=13.4, elevation=13.9))

    gf.add_edge(Edge(id="01", name="C01", inicial_id="01", final_id="02", diameter=100, material="PVC"))
    
    gf.print_this()