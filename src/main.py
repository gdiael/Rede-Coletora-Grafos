from graph import Graph
from line_graph import generate_line_graph

if __name__ == "__main__":
    testname = "grafo_01"

    gf = Graph.load_from_file(f"dataset/{testname}.txt")
    gf.print_this()

    lgf = generate_line_graph(gf)
    lgf.print_this()
