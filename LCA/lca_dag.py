import networkx as nx

"""
class LCA_Dag:
method: 
finds lowest common ancestors for two nodes inside a directed cyclic graph
find_lca(graph, a, b):
"""


class LcaDag:
    """
    graph is defined and populated using networkx library. first all of the ancestors of a and b are found
    among them, the common ancestors are selected including a and b themselves. Lcas are found by the fact that the lca
    is the vertices which has the shortest cumulative distance from it to a and b, ie. the vertices with the highest
    depth to a and b. The shortest path are found using networkx's built in methods which by default uses dijkstra's
    shortest path algorithm. The lcas are populated into a list
    :parameter
    graph : a none empty and not None direct acyclic graph object defined by networkx library
    a : a vertex in the graph
    b : another different vertex in the graph

    :returns
    error : error message as a string identifying error cases
    lcas : a list of vertices in graph which are the lcas of vertex a and b
    """
    def find_lca(self, graph, a, b):
        if graph is None or nx.is_empty(graph):
            return "graph is empty"

        if not nx.is_directed_acyclic_graph(graph):
            return "graph is not dag"

        try:
            anc_a = nx.ancestors(graph, a)
            anc_b = nx.ancestors(graph, b)
            anc_a.add(a)
            anc_b.add(b)

            common_anc = anc_a.intersection(anc_b)
            if len(common_anc) <= 0:
                return "no lcas can be found"

            common_anc = list(common_anc)
            lcas = list()
            min_path = 0
            for i in range(len(common_anc)):
                t = nx.shortest_path_length(graph, common_anc[i], a) + nx.shortest_path_length(graph, common_anc[i], b)
                if i != 0:
                    if t < min_path:
                        lcas.clear()
                        min_path = t
                        lcas.append(common_anc[i])
                    elif t == min_path:
                        lcas.append(common_anc[i])
                else:
                    min_path = t
                    lcas.append(common_anc[i])
            return lcas
        except nx.exception.NetworkXError as error:
            return str(error)


def main():
    g = nx.DiGraph()
    edges = list()
    file = open("../resources/ten_node_dag.txt", 'r')
    for lines in file:
        values = lines.split(" ")
        edges.append(tuple(values))
    file.close()
    g.add_weighted_edges_from(edges)
    k = LcaDag().find_lca(g, "12", "12")
    print(str(k))

if __name__ == '__main__':
    main()
