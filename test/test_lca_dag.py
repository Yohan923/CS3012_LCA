import unittest
import networkx as nx
from LCA.lca_dag import LcaDag


class TestLcaDag(unittest.TestCase):

    def setUp(self):
        # read data to create dag with ten nodes
        g = nx.DiGraph()
        edges = list()
        file = open("../resources/ten_node_dag.txt", 'r')
        for lines in file:
            values = lines.split(" ")
            edges.append(tuple(values))
        file.close()
        g.add_weighted_edges_from(edges)
        self.ten_node_dag = g

        # read data to create cyclic directed graphs
        g = nx.DiGraph()
        edges = list()
        file = open("../resources/cyclic_directed_graph.txt", 'r')
        for lines in file:
            values = lines.split(" ")
            edges.append(tuple(values))
        file.close()
        g.add_weighted_edges_from(edges)
        self.cyclic_directed_graph = g

        # create empty graph
        self.empty_dag = nx.DiGraph()

    def test_find_lca(self):
        # test normal case with only one lca for inputs a, b
        self.assertEqual(["12"], LcaDag().find_lca(self.ten_node_dag, "14", "12"))
        # test normal case with a == b
        self.assertEqual(["12"], LcaDag().find_lca(self.ten_node_dag, "12", "12"))
        # test normal case with multiple lcas for inputs a, b
        result = LcaDag().find_lca(self.ten_node_dag, "9", "10")
        result = set(result)
        expected = {"6", "8"}
        self.assertEqual(set(), expected.difference(result))
        # test cases when one or two nodes are not found in the graph
        self.assertEqual("The node 0 is not in the graph.", LcaDag().find_lca(self.ten_node_dag, "0", "12"))
        self.assertEqual("The node 0 is not in the graph.", LcaDag().find_lca(self.ten_node_dag, "12", "0"))
        # test case where the graph is not a dag ie. directed graph with cycles
        self.assertEqual("graph is not dag", LcaDag().find_lca(self.cyclic_directed_graph, "1", "2"))
        # test empty graph
        self.assertEqual("graph is empty", LcaDag().find_lca(self.empty_dag, "1", "12"))
