import networkx as nx

class LCA_Dag:

    def find_lca(self, graph, a, b):
        return 0


def main():
    G = nx.Graph()
    G.add_node(1)

    print(list(nx.connected_components(G)))


if __name__ == '__main__':
    main()