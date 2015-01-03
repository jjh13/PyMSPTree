#!/usr/bin/env python
""" Multi-resolution Sphere Packing tree

This file contains an implementation of
    Multi-resolution sphere packing tree: a hierarchical multi-resolution 3D data structure
        Jiro Inoue          Queen's University, Ontario, Canada
        A. James Stewart    Queen's University, Ontario, Canada

    @author Joshua Horacsek
"""


class MSPTreeType:
    """ Defines how the MSP will be used, a function space has a coefficient at each level of the tree for use with
    a hierarchical reconstruction scheme. A space partitioning tree just partitions space so only the last node contains
    a bin in which a value is stored.
    """
    FunctionSpace, SpacePartitioning = range(2)

    def __init__(self):
        pass


class MSPTree(object):
    """ MSP Tree Implementation
    """

    class _NodeType:
        CC_Node, BCC_Node, FCC_Node = range(3)

        def __init__(self):
            pass

    class _NodeColor:
        Node_Red, Node_Green, Node_Blue, Node_Yellow, Node_Ghost = range(5)

        def __init__(self):
            pass

    class _Node:

        def __init__(self, position, color,  value=None):
            """
            """
            self.value = value
            self.position = position
            self.expanded = False
            self.color = color
            self.lattice = None

        def expand_node(self, depth, scale):
            """
            """
            pass

        def expand_cc_node(self, depth, scale):
            """
            """
            pass

        def expand_bcc_node(self, depth, scale):
            """
            """
            pass

    def __init__(self, max_depth, tree_type=MSPTreeType.FunctionSpace):
        """
        """
        self.roots = [];

    def find_closest_node(point, level=-1):
        pass

    def expand_to(point):
        pass

