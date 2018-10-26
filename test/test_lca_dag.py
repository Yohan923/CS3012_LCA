import  unittest
import networkx as nx
from LCA.lca_dag import LCA_Dag

class TestLcaDag(unittest.TestCase):

    def setUp(self):
        g = nx.DiGraph()
        edges = list()
        file = open("../resources/ten_node_dag.txt", 'r')
        for lines in file:
            values = lines.split(" ")
            edges.append(tuple(values))
        file.close()

        g.add_weighted_edges_from(edges)

        self.ten_node_dag = g
        self.empty_dag = nx.DiGraph()

    def test_find_lca(self):
        self.assertEqual(["12"], LCA_Dag().find_lca(self.ten_node_dag, "14", "12"))

        result = LCA_Dag().find_lca(self.ten_node_dag, "9", "10")
        result = set(result)
        expected = {"6", "8"}
        self.assertEqual(set(), expected.difference(result))

        self.assertEqual("The node 0 is not in the graph.", str(LCA_Dag().find_lca(self.ten_node_dag, "0", "12")))
        self.assertEqual("The node 0 is not in the graph.", str(LCA_Dag().find_lca(self.ten_node_dag, "12", "0")))

        self.assertEqual("graph is empty", LCA_Dag().find_lca(self.empty_dag, "1", "12"))
