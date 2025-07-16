from graph import Graph
from vertex import Vertex
from edge import Edge

def generate_line_graph(gf: Graph) -> Graph:
    lgf = Graph(f"{gf.name} - line")

    vertex_dict = gf.get_vertices()
    edge_dict = gf.get_edges()

    edge_ids = []

    for edge_id, edge in edge_dict.items():
        edge.update_weight(vertex_dict)
        
        lgf.add_vertex(Vertex(
            id=edge_id,
            name=edge.name,
            x=0.0, y=0.0, elevation=0.0,
            description=f"Represents {edge_id} edge"
        ))

        edge_ids.append(edge_id)
    
    for i in range(len(edge_ids)):
        e1 = edge_dict[edge_ids[i]]
        for j in range(i + 1, len(edge_ids)):
            e2 = edge_dict[edge_ids[j]]
            if e1.is_adjacent(e2):
                lgf.add_edge(Edge(
                    id=f"{e1.id}_{e2.id}",
                    name=f"{e1.name}-{e2.name}",
                    inicial_id=e1.id,
                    final_id=e2.id,
                    diameter=0,
                    material="virtual",
                    description=f"Edge for {e1.id} and {e2.id}",
                    weight=e1.weight + e2.weight
                ))

    return lgf