#!/usr/bin/env python
""" Multi-resolution Sphere Packing Tree

This file contains an implementation of
    Multi-resolution sphere packing tree: a hierarchical multi-resolution 3D data structure
        Jiro Inoue          Queen's University, Ontario, Canada
        A. James Stewart    Queen's University, Ontario, Canada


 @author Joshua Horacsek, Simon Fraser University, Burnaby, Canada
 @version 0.1
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

        def __init__(self, position, color, value=None):
            """
            """
            if value is not None:
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
        """ Initializes the tree, whose default expansion is the unit CC
        grid with the 27 points in {-1,0,1}^3
        """
        self.roots = [
            self._Node((0, 0, 0), self._NodeColor.Node_Red),

            # Green nodes
            self._Node((1, 1, 1), self._NodeColor.Node_Green),
            self._Node((1, 1, -1), self._NodeColor.Node_Green),
            self._Node((1, -1, 1), self._NodeColor.Node_Green),
            self._Node((1, -1, -1), self._NodeColor.Node_Green),
            self._Node((-1, 1, 1), self._NodeColor.Node_Green),
            self._Node((-1, 1, -1), self._NodeColor.Node_Green),
            self._Node((-1, -1, 1), self._NodeColor.Node_Green),
            self._Node((-1, -1, -1), self._NodeColor.Node_Green),

            # Blue nodes
            self._Node((-1, 1, 0), self._NodeColor.Node_Blue),
            self._Node((-1, 0, 1), self._NodeColor.Node_Blue),
            self._Node((-1, 0, -1), self._NodeColor.Node_Blue),
            self._Node((-1, -1, 0), self._NodeColor.Node_Blue),

            self._Node((0, 1, 1), self._NodeColor.Node_Blue),
            self._Node((0, 1, -1), self._NodeColor.Node_Blue),
            self._Node((0, -1, 1), self._NodeColor.Node_Blue),
            self._Node((0, -1, -1), self._NodeColor.Node_Blue),

            self._Node((1, 1, 0), self._NodeColor.Node_Blue),
            self._Node((1, 0, 1), self._NodeColor.Node_Blue),
            self._Node((1, 0, -1), self._NodeColor.Node_Blue),
            self._Node((1, -1, 0), self._NodeColor.Node_Blue),

            # Yellow nodes
            self._Node((1, 0, 0), self._NodeColor.Node_Yellow),
            self._Node((-1, 0, 0), self._NodeColor.Node_Yellow),
            self._Node((0, 1, 0), self._NodeColor.Node_Yellow),
            self._Node((0, -1, 0), self._NodeColor.Node_Yellow),
            self._Node((0, 0, 1), self._NodeColor.Node_Yellow),
            self._Node((0, 0, -1), self._NodeColor.Node_Yellow),
        ]

        self.max_depth = max_depth
        self.tree_type = tree_type

    def find_closest_node(point, level=-1):
        pass

    def expand_to(point):
        pass

