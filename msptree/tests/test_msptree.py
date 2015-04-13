import unittest
from .. msptree import *


class TestMSPTree(unittest.TestCase):

    def test_init(self):
        tree = MSPTree(12)

        self.assertEquals(len(tree.roots), 27)

    def text_expand_all_8(self):
        pass

    def test_expansion(self):
        pass



if __name__ == '__main__':
    unittest.main()