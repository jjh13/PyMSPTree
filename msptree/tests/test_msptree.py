import unittest
from .. msptree import MSPTree, _NodeType, _NodeColor


def export_obj(tree, output):
    def traverse(node, filep):
        if len(node.children) == 0:
            p = node.position
            if -1 <= p[0] <= 1 and -1 <= p[1] <= 1 and -1 <= p[2] <= 1 and node.color != _NodeColor.Node_Ghost:
                filep.write('v %f %f %f \n' % (p[0], p[1], p[2]))
        else:
            for child in node.children:
                traverse(child, filep)

    fh = open(output, 'w')
    for root in tree.roots:
        traverse(root, fh)
    fh.close()


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

        self.assertEquals(nd.lattice, _NodeType.CC_Node)

    def test_root_expansion(self):
        tree = MSPTree(12)

        nd = tree.find_closest_node((0.1, 0.1, 0.1))
        nd.expand_node()

    def text_expand_all_8(self):
        pass

    def test_expansion(self):
        pass

    def test_export_obj(self):
        tree = MSPTree(12)

        export_obj(tree, 'msp_no_exp.obj')

        nd = tree.find_closest_node((0, 0, 0))
        nd.expand_node()

        export_obj(tree, 'msp_000_exp.obj')

    def test_export_first_level_expand(self):
        tree = MSPTree(12)

        for root in tree.roots:
            root.expand_node()

        export_obj(tree, 'msp_lv1_exp.obj')

    def test_export_second_level_expand(self):
        tree = MSPTree(12)

        for root in tree.roots:
            root.expand_node()
            for child in root.children:
                child.expand_node()

        export_obj(tree, 'msp_lv2_exp.obj')

    def test_export_third_level_expand(self):
        tree = MSPTree(12)

        for root in tree.roots:
            root.expand_node()
            for child in root.children:
                child.expand_node()
                for grandchild in child.children:
                    grandchild.expand_node()

        export_obj(tree, 'msp_lv3_exp.obj')

    def test_export_fourth_level_expand(self):
        tree = MSPTree(12)

        for root in tree.roots:
            root.expand_node()
            for child in root.children:
                child.expand_node()
                if child.scale != 1.0:
                    print ('ch', child.scale, 1.0, child.color, child.lattice)
                for grandchild in child.children:
                    grandchild.expand_node()

                    if grandchild.scale != 0.5:
                        print ('gc', grandchild.scale, 0.5, grandchild.color, grandchild.lattice)
                    for ggc in grandchild.children:
                        ggc.expand_node()
                        if ggc.scale != 0.5:
                            print ('ggc', ggc.scale, 0.5, ggc.color, ggc.lattice)

        export_obj(tree, 'msp_lv4_exp.obj')

    def test_center_expand(self):
        tree = MSPTree(12)

        print 'dont be greedy'
        nd = tree.find_closest_node((0, 0, 0))
        nd.expand_node()
        export_obj(tree, 'msp_c0_exp.obj')

        nd = tree.find_closest_node((0, 0, 0))
        nd.expand_node()
        export_obj(tree, 'msp_c1_exp.obj')

        nd = tree.find_closest_node((0, 0, 0))
        nd.expand_node()
        export_obj(tree, 'msp_c2_exp.obj')

        nd = tree.find_closest_node((0, 0, 0))
        nd.expand_node()
        export_obj(tree, 'msp_c3_exp.obj')

        nd = tree.find_closest_node((0, 0, 0))
        nd.expand_node()
        export_obj(tree, 'msp_c4_exp.obj')


if __name__ == '__main__':
    unittest.main()