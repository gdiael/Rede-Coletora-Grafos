from graph import Graph
from line_graph import generate_line_graph
from mst_graph import minimum_spanning_tree
from dfs_edges import dfs_update_edges
import time

if __name__ == "__main__":

    def optimize_graph(gf: Graph) -> Graph:
        start_time = time.time()
        total_weight = -1.0

        for i in range(1, 9):
            print()
            print(f"Processing graph: step {i}...")
            print()

            lgf = generate_line_graph(gf)
            mst = minimum_spanning_tree(lgf)

            start_vertex_id = min(gf.get_vertices(), key=lambda vid: gf.get_vertices()[vid].elevation)
            dfs_update_edges(gf, mst, start_vertex_id)

            local_weight = gf.get_total_weight()
            print(f"Local weight of the graph for this step: {local_weight:.3f}")

            # gf.print_this()

            if total_weight < 0.0 or local_weight < total_weight:
                total_weight = local_weight
                gfinal = gf.copy_me()

        gfinal.name = f"{gf.name} - otm"
        time_taken_ms = (time.time() - start_time) * 1000
        gfinal.observation = f"Optimized in {time_taken_ms:.4f} ms"

        return gfinal

    graphName = input("Digite o nome do arquivo do grafo (ex: grafo_01): ").strip()

    gf = Graph.load_from_file(f"dataset/{graphName}.txt")

    if input("Deseja imprimir o grafo carregado? (s/n): ").strip().lower() == 's':
        gf.print_this()

    if input("Deseja fazer a otimização do grafo? (s/n): ").strip().lower() == 's':
        gfinal = optimize_graph(gf)

        if (input("Deseja imprimir o grafo otimizado? (s/n): ").strip().lower() == 's'):
            print(f"Final graph: {gfinal.name} - {gfinal.observation}")
            gfinal.print_this()

        if input("Deseja salvar o grafo otimizado? (s/n): ").strip().lower() == 's':
            gfinal.save_to_file("dataset")
            print(f"Grafo otimizado salvo como: dataset/{gfinal.name}.txt")

