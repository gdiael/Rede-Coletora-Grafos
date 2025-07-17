from graph import Graph
import heapq

def get_new_vertex(edge, visited):
    v1 = edge.inicial_id
    v2 = edge.final_id
    if v1 in visited and v2 not in visited:
        return v2
    elif v2 in visited and v1 not in visited:
        return v1
    return None

def add_connected_edges(edge_heap, edges, new_vertex, visited):
    for next_edge in edges.values():
        if ((next_edge.inicial_id == new_vertex and next_edge.final_id not in visited) or
            (next_edge.final_id == new_vertex and next_edge.inicial_id not in visited)):
            heapq.heappush(edge_heap, (next_edge.weight, next_edge))

def minimum_spanning_tree(gf: Graph) -> Graph:
    mst = Graph(f"{gf.name} - mst")
    vertices = gf.get_vertices()
    edges = gf.get_edges()

    for v in vertices.values():
        mst.add_vertex(v)

    if not vertices:
        return mst

    start_id = next(iter(vertices))
    visited = {start_id}
    edge_heap = []

    for edge in edges.values():
        if edge.inicial_id == start_id or edge.final_id == start_id:
            heapq.heappush(edge_heap, (edge.weight, edge))

    while edge_heap and len(visited) < len(vertices):
        _, edge = heapq.heappop(edge_heap)
        new_vertex = get_new_vertex(edge, visited)
        if new_vertex is None:
            continue

        mst.add_edge(edge)
        visited.add(new_vertex)
        add_connected_edges(edge_heap, edges, new_vertex, visited)

    return mst