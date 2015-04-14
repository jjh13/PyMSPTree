import unittest
from .. msptree import *


class TestMSPTree(unittest.TestCase):

    def test_init(self):
        tree = MSPTree(12)

        self.assertEquals(len(tree.roots), 27)

    def test_node_position(self):
        tree = MSPTree(12)

        nd = tree.find_closest_node((1.1, 1.1, 1.1))
        self.assertEquals(nd.position, (1, 1, 1))

        nd = tree.find_closest_node((0.1, 0.1, 0.1))
        self.assertEquals(nd.position, (0, 0, 0))

    def text_expand_all_8(self):
        pass

    def test_expansion(self):
        pass


if __name__ == '__main__':
    unittest.main()