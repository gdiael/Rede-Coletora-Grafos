from graph import Graph
from line_graph import generate_line_graph
from mst_graph import minimum_spanning_tree
from dfs_edges import dfs_update_edges

if __name__ == "__main__":
    testname = "grafo_01"

    gf = Graph.load_from_file(f"dataset/{testname}.txt")
    gf.print_this()

    total_weight = -1.0

    for i in range(1, 6):
        print()
        print(f"Processing graph: step {i}...")
        print()

        lgf = generate_line_graph(gf)

        mst = minimum_spanning_tree(lgf)
        mst.print_this()

        start_vertex_id = min(gf.get_vertices(), key=lambda vid: gf.get_vertices()[vid].elevation)

        dfs_update_edges(gf, mst, start_vertex_id)
        
        local_weight = gf.get_total_weight()
        print(f"Local weight of the graph for this step: {local_weight:.3f}")

        if total_weight < 0.0:
            total_weight = local_weight
        else:
            if local_weight < total_weight: 
                total_weight = local_weight
            else:
                print("No improvement in weight, stopping the process.")
                break
        
        gf.print_this()

        gfinal = gf.copy_me()

    print("Final graph:")
    gfinal.print_this()
