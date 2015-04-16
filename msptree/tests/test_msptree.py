import unittest
from .. msptree import MSPTree, _NodeType, _NodeColor
import random
import math

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


def export_obj_normal(tree, output):
    def traverse(node, filep):
        if len(node.children) == 0:
            p = node.position
            if -1 <= p[0] <= 1 and -1 <= p[1] <= 1 and -1 <= p[2] <= 1 and \
                    node.color != _NodeColor.Node_Ghost and\
                    hasattr(node, 'value') and \
                    node.value is not None:

                n = node.value
                filep.write('v %f %f %f \n' % (p[0], p[1], p[2]))
                filep.write('vn %f %f %f \n' % (n[0], n[1], n[2]))
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
                for grandchild in child.children:
                    grandchild.expand_node()
                    for ggc in grandchild.children:
                        ggc.expand_node()

        export_obj(tree, 'msp_lv4_exp.obj')


    def test_export_seventh_level_expand(self):
        tree = MSPTree(12)

        for root in tree.roots:
            root.expand_node()
            for child in root.children:
                child.expand_node()
                for grandchild in child.children:
                    grandchild.expand_node()
                    for ggc in grandchild.children:
                        ggc.expand_node()

                        for gggc in ggc.children:
                            gggc.expand_node()

                            for ggggc in gggc.children:
                                ggggc.expand_node()

                                for gggggc in ggggc.children:
                                    gggggc.expand_node()

        export_obj(tree, 'msp_lv7_exp.obj')

    def test_center_expand(self):
        tree = MSPTree(12)

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



    def test_sphere_expansion(self):
        samples = 100000
        tree = MSPTree(15)

        f = open('out.obj', 'w')

        for _ in xrange(samples):
            z = 2*random.random() - 1
            theta = 2*math.pi*random.random() - math.pi
            x = math.sin(theta)*math.sqrt(1-z*z)
            y = math.cos(theta)*math.sqrt(1-z*z)

            tree.expand_to((x,y,z)).value = (x,y,z)
            f.write("v %f %f %f \n" % (x,y,z))
        f.close()
        export_obj_normal(tree, 'tree_sphere.obj')


if __name__ == '__main__':
    unittest.main()