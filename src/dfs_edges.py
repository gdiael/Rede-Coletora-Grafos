from graph import Graph
from vertex import Vertex
from edge import Edge

from config import MINIMUM_DEPTH, MINIMUM_SLOP

def get_edge_adjacency_dict(gf: Graph, lfg: Graph) -> dict[str, set]:
    edge_adjacency = {v.id: set() for v in gf.get_vertices().values()}
    edges = gf.get_edges()
    for edge in lfg.get_edges().values():
        e1 = edges[edge.inicial_id]
        e2 = edges[edge.final_id]
        if e1.inicial_id == e2.inicial_id or e1.inicial_id == e2.final_id:
            vid = e1.inicial_id
        elif e1.final_id == e2.final_id or e1.final_id == e2.inicial_id:
            vid = e1.final_id
        else:
            continue
        edge_adjacency[vid].add(edge.inicial_id)
        edge_adjacency[vid].add(edge.final_id)
    return edge_adjacency

def update_depth(edge: Edge, vertices: dict[str, Vertex], depth_list: dict[str, float], is_leaf: bool):
    if edge.inicial_depth < MINIMUM_DEPTH:
        edge.inicial_depth = MINIMUM_DEPTH
    if edge.final_depth < MINIMUM_DEPTH:
        edge.final_depth = MINIMUM_DEPTH

    if edge.inicial_depth < depth_list[edge.inicial_id] and not is_leaf:
        edge.inicial_depth = depth_list[edge.inicial_id]

    length = edge.get_horizontal_length(vertices)
    slop = edge.get_slope(vertices)
    if slop < MINIMUM_SLOP:
        delta_terr = vertices[edge.inicial_id].elevation - vertices[edge.final_id].elevation
        delta_depth_min = length * MINIMUM_SLOP
        delta_depth_att = edge.inicial_depth - edge.final_depth
        edge.final_depth += delta_depth_min - delta_terr + delta_depth_att
    if depth_list[edge.inicial_id] < edge.inicial_depth:
        depth_list[edge.inicial_id] = edge.inicial_depth
    if depth_list[edge.final_id] < edge.final_depth:
        depth_list[edge.final_id] = edge.final_depth

def dfs_update_edges(grafo: Graph, grafo_linha: Graph, root_id: str):
    grafo.reset_depth()
    edges = grafo.get_edges()
    vertices = grafo.get_vertices()
    visited_edges = set()
    depth_stack = [(root_id, "None")]  # (current_vertex_id, edge_from_parent)
    return_stack = []

    depth_list = {v.id: 0.0 for v in grafo.get_vertices().values()}

    edge_adjacency_dict = get_edge_adjacency_dict(grafo, grafo_linha)

    while depth_stack:
        current_id, from_edge = depth_stack.pop()

        print(f"Visiting vertex: {current_id}, from edge: {from_edge}")

        is_leaf = True

        for edge_id in edge_adjacency_dict[current_id]:
            if edge_id in visited_edges:
                continue
            print(f"Checking edge: {edge_id} from vertex: {current_id}")
            
            adj_edge = edges[edge_id]
            if current_id != adj_edge.final_id:
                adj_edge.reverse()

            depth_stack.append((adj_edge.inicial_id, edge_id))
            visited_edges.add(edge_id)
            is_leaf = False

        if from_edge != "None":
            return_stack.append((from_edge, is_leaf))

    # Processa em pós-ordem (volta) para calcular profundidades
    while return_stack:
        edge_id, is_leaf = return_stack.pop()
        print(f"Updating edge: {edge_id} in return stack")
        curr_edge = edges[edge_id]
        update_depth(curr_edge, vertices, depth_list, is_leaf)
