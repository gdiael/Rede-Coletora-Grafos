from vertex import Vertex
from edge import Edge
from graph import Graph

if __name__ == "__main__":
    testname = "grafo_01"

    # gf = Graph(testname)
    
    # gf.add_vertex(Vertex(id="01", name="PV01", x=11.5, y=60.4, elevation=12.9))
    # gf.add_vertex(Vertex(id="02", name="PV02", x=72.8, y=61.3, elevation=13.9))
    # gf.add_vertex(Vertex(id="03", name="PV03", x=133.1, y=62.1, elevation=9.2))
    # gf.add_vertex(Vertex(id="04", name="PV04", x=10.1, y=3.7, elevation=10.4))
    # gf.add_vertex(Vertex(id="05", name="PV05", x=71.5, y=2.9, elevation=9.8))
    # gf.add_vertex(Vertex(id="06", name="PV06", x=134.6, y=4.1, elevation=7.8))

    # gf.add_edge(Edge(id="01", name="C01", inicial_id="01", final_id="02", diameter=150, material="PVC"))
    # gf.add_edge(Edge(id="02", name="C02", inicial_id="02", final_id="03", diameter=150, material="PVC"))
    # gf.add_edge(Edge(id="03", name="C03", inicial_id="01", final_id="04", diameter=100, material="PVC"))
    # gf.add_edge(Edge(id="04", name="C04", inicial_id="02", final_id="05", diameter=100, material="PVC"))
    # gf.add_edge(Edge(id="05", name="C05", inicial_id="03", final_id="06", diameter=100, material="PVC"))
    # gf.add_edge(Edge(id="06", name="C06", inicial_id="04", final_id="05", diameter=100, material="PVC"))
    # gf.add_edge(Edge(id="07", name="C07", inicial_id="05", final_id="06", diameter=100, material="PVC"))

    # gf.save_to_file("dataset")

    gf2 = Graph.load_from_file(f"dataset/{testname}.txt")
    gf2.print_this()
