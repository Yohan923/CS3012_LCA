import networkx as nx


class LCA_Dag:

    def find_lca(self, graph, a, b):
        if graph is not None:
            if nx.is_directed_acyclic_graph(graph):
                anc_a = nx.ancestors(graph, a)
                anc_b = nx.ancestors(graph, b)
                anc_a.add(a)
                anc_b.add(b)

                common_anc = anc_a.intersection(anc_b)
                lcas = list()
                min_path = 0
                for i in common_anc:
                    t = nx.shortest_path_length(graph, i, a) + nx.shortest_path_length(graph, i, b)
                    if min_path != 0:
                        if min_path > t:
                            lcas.clear()
                            min_path = t
                            lcas.append(i)
                        elif min_path == t:
                            lcas.append(i)
                    else:
                        min_path = t
                        lcas.append(i)
                return lcas
            else:
                return "graph is not dag"
        else:
            return "graph is empty"


def main():
    G = nx.DiGraph()
    edges = list()
    file = open("../resources/ten_node_dag.txt", 'r')
    for lines in file:
        values = lines.split(" ")
        edges.append(tuple(values))
    file.close()

    G.add_weighted_edges_from(edges)

    print(LCA_Dag().find_lca(G, "12", "14"))


if __name__ == '__main__':
    main()
