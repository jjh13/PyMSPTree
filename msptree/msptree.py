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
   
    
class _NodeType:
    CC_Node, BCC_Node, FCC_Node = range(3)

    def __init__(self):
        pass


class _NodeColor:
    Node_Red, Node_Green, Node_Blue, Node_Yellow, Node_Ghost = range(5)

    def __init__(self):
        pass


class MSPNodeException(Exception):

    def __init__(self, text, node):
        self.error = text
        self.node = node

    def __str__(self):
        pass


class MSPTree(object):
    """ MSP Tree Implementation
    """

    class _Node:

        def __init__(self, position, color, lattice_type, value=None):
            """

            """
            if value is not None:
                self.value = value
            self.position = position
            self.color = color
            self.lattice = lattice_type
            self.children = []

        def __unicode__(self):
            return "Node at %s" % str(self.position)

        def __str__(self):
            return "Node at %s" % str(self.position)

        def find_closest_node(self, point):
            dot = lambda x, y: abs((x[0]-y[0])*(x[0] - y[0]) + (x[1]-y[1])*(x[1] - y[1]) + (x[2]-y[2])*(x[2]-y[2]))
            if len(self.children) <= 0:
                return self
            node = min([(dot(point, n.position), n) for n in self.children], key=lambda x: x[0])[1]
            return node.find_closest_node(point)

        def expand_to(self, point, depth=0, max_depth=12):
            dot = lambda x, y: abs((x[0]-y[0])*(x[0] - y[0]) + (x[1]-y[1])*(x[1] - y[1]) + (x[2]-y[2])*(x[2]-y[2]))
            if depth >= max_depth:
                return

            if len(self.children) <= 0:
                scale = 0.5**int(depth/3)
                self.expand_node(depth, scale)

            node = min([(dot(point, n.position), n) for n in self.children], key=lambda x: x[0])[1]
            node.expand_to(point, depth+1, max_depth)

        def expand_node(self, depth, scale):
            """
            Expands this node depending on its type
            """
            if len(self.children) > 0 or depth <= 0:
                return

            if self.lattice == _NodeType.CC_Node:
                self._expand_cc_node(depth, scale)
            elif self.lattice == _NodeType.BCC_Node:
                self._expand_bcc_node(depth, scale)
            elif self.lattice == _NodeType.FCC_Node:
                self._expand_fcc_node(depth, scale)
            else:
                raise MSPNodeException("Tree node had an invalid lattice type.", self)

        @staticmethod
        def _aas(a, b, scale):
            return a[0] + b[0]*scale, a[1]+b[1]*scale, a[2]+b[2]*scale

        def _expand_cc_node(self, depth, scale):
            o = self.position
            if self.color == _NodeColor.Node_Red:
                self.children = [

                    MSPTree._Node(o, _NodeColor.Node_Red, _NodeType.FCC_Node),

                    # Add child blue nodes
                    MSPTree._Node(self._aas(o, (-0.5, 0.5, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, 0.0, 0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, -0.5, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, 0.0, -0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),

                    MSPTree._Node(self._aas(o, (0.0, 0.5, 0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.5, -0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.0, -0.5, 0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.0, -0.5, -0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),

                    MSPTree._Node(self._aas(o, (0.5, 0.5, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, 0.0, 0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, -0.5, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, 0.0, -0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),

                    # Add ghost nodes
                    MSPTree._Node(self._aas(o, (0.5, 0.5, 0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, 0.5, -0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, -0.5, 0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, -0.5, -0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),

                    MSPTree._Node(self._aas(o, (-0.5, 0.5, 0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, 0.5, -0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, -0.5, 0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, -0.5, -0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                ]
            elif self.color == _NodeColor.Node_Green:
                self.children = [

                    MSPTree._Node(o, _NodeColor.Node_Green, _NodeType.FCC_Node),

                    # Add child blue nodes
                    MSPTree._Node(self._aas(o, (-0.5, 0.5, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, 0.0, 0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, -0.5, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, 0.0, -0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),

                    MSPTree._Node(self._aas(o, (0.0, 0.5, 0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.5, -0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.0, -0.5, 0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.0, -0.5, -0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),

                    MSPTree._Node(self._aas(o, (0.5, 0.5, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, 0.0, 0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, -0.5, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, 0.0, -0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.FCC_Node),

                    # Add ghost nodes
                    MSPTree._Node(self._aas(o, (0.5, 0.5, 0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, 0.5, -0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, -0.5, 0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (0.5, -0.5, -0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),

                    MSPTree._Node(self._aas(o, (-0.5, 0.5, 0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, 0.5, -0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, -0.5, 0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                    MSPTree._Node(self._aas(o, (-0.5, -0.5, -0.5), scale),
                                  _NodeColor.Node_Ghost, _NodeType.FCC_Node),
                ]
            elif self.color == _NodeColor.Node_Blue:
                self.children = [
                    MSPTree._Node(o, _NodeColor.Node_Red, _NodeType.FCC_Node),
                ]
            elif self.color == _NodeColor.Node_Yellow:
                self.children = [
                    MSPTree._Node(o, _NodeColor.Node_Green, _NodeType.FCC_Node)
                ]
            else:
                raise MSPNodeException("Attempted to expand an invalid node color", self)

        def _expand_fcc_node(self, depth, scale):
            o = self.position
            if self.color == _NodeColor.Node_Red:
                self.children = [

                    MSPTree._Node(o, _NodeColor.Node_Red, _NodeType.BCC_Node),

                    # These cases are based on parity, check the paper
                    MSPTree._Node(self._aas(o, (0.25, 0.25, 0.25), scale),
                                  _NodeColor.Node_Yellow, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (0.25, 0.25, -0.25), scale),
                                  _NodeColor.Node_Green, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (0.25, -0.25, 0.25), scale),
                                  _NodeColor.Node_Green, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (0.25, -0.25, -0.25), scale),
                                  _NodeColor.Node_Yellow, _NodeType.BCC_Node),

                    MSPTree._Node(self._aas(o, (-0.25, 0.25, -0.25), scale),
                                  _NodeColor.Node_Yellow, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (-0.25, 0.25, 0.25), scale),
                                  _NodeColor.Node_Green, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (-0.25, -0.25, -0.25), scale),
                                  _NodeColor.Node_Green, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (-0.25, -0.25, 0.25), scale),
                                  _NodeColor.Node_Yellow, _NodeType.BCC_Node),

                    MSPTree._Node(self._aas(o, (0.5, 0.0, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.5, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.0, 0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.BCC_Node),

                    MSPTree._Node(self._aas(o, (-0.5, 0.0, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (0.0, -0.5, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.0, -0.5), scale),
                                  _NodeColor.Node_Blue, _NodeType.BCC_Node),

                ]
            elif self.color == _NodeColor.Node_Green:
                self.children = [

                    MSPTree._Node(o, _NodeColor.Node_Red, _NodeType.BCC_Node),

                    MSPTree._Node(self._aas(o, (0.25, 0.25, 0.25), scale),
                                  _NodeColor.Node_Yellow, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (0.25, 0.25, -0.25), scale),
                                  _NodeColor.Node_Green, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (0.25, -0.25, 0.25), scale),
                                  _NodeColor.Node_Green, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (0.25, -0.25, -0.25), scale),
                                  _NodeColor.Node_Yellow, _NodeType.BCC_Node),

                    MSPTree._Node(self._aas(o, (-0.25, 0.25, -0.25), scale),
                                  _NodeColor.Node_Yellow, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (-0.25, 0.25, 0.25), scale),
                                  _NodeColor.Node_Green, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (-0.25, -0.25, -0.25), scale),
                                  _NodeColor.Node_Green, _NodeType.BCC_Node),
                    MSPTree._Node(self._aas(o, (-0.25, -0.25, 0.25), scale),
                                  _NodeColor.Node_Yellow, _NodeType.BCC_Node),
                ]
            elif self.color == _NodeColor.Node_Blue:
                self.children = [
                    MSPTree._Node(o, _NodeColor.Node_Red, _NodeType.BCC_Node)
                ]
            elif self.color == _NodeColor.Yellow:
                self.children = [
                    MSPTree._Node(o, _NodeColor.Node_Green, _NodeType.BCC_Node)
                ]
            else:
                raise MSPNodeException("Attempted to expand an invalid node color", self)

        def _expand_bcc_node(self, depth, scale):
            o = self.position
            if self.color == _NodeColor.Node_Red:
                self.children = [

                    MSPTree._Node(o, _NodeColor.Node_Red, _NodeType.CC_Node),

                    MSPTree._Node(self._aas(o, (0.25, 0.0, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.25, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.0, 0.25), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),

                    MSPTree._Node(self._aas(o, (-0.25, 0.0, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),
                    MSPTree._Node(self._aas(o, (0.0, -0.25, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.0, -0.25), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),

                ]
            elif self.color == _NodeColor.Node_Green:
                self.children = [

                    MSPTree._Node(o, _NodeColor.Node_Green, _NodeType.CC_Node),

                    MSPTree._Node(self._aas(o, (0.25, 0.0, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.25, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.0, 0.25), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),

                    MSPTree._Node(self._aas(o, (-0.25, 0.0, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),
                    MSPTree._Node(self._aas(o, (0.0, -0.25, 0.0), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),
                    MSPTree._Node(self._aas(o, (0.0, 0.0, -0.25), scale),
                                  _NodeColor.Node_Blue, _NodeType.CC_Node),

                ]
            elif self.color == _NodeColor.Node_Blue:
                self.children = [
                    MSPTree._Node(o, _NodeColor.Node_Red, _NodeType.CC_Node)
                ]
            elif self.color == _NodeColor.Yellow:
                self.children = [
                    MSPTree._Node(o, _NodeColor.Node_Green, _NodeType.CC_Node)
                ]
            else:
                raise MSPNodeException("Attempted to expand an invalid node color", self)

    #
    #
    #

    def __init__(self, max_depth, tree_type=MSPTreeType.FunctionSpace):
        """ Initializes the tree, whose default expansion is the unit CC
        grid with the 27 points in {-1,0,1}^3
        """
        self.roots = [
            self._Node((0, 0, 0), _NodeColor.Node_Red, _NodeType.CC_Node),

            # Green nodes
            self._Node((1, 1, 1), _NodeColor.Node_Green, _NodeType.CC_Node),
            self._Node((1, 1, -1), _NodeColor.Node_Green, _NodeType.CC_Node),
            self._Node((1, -1, 1), _NodeColor.Node_Green, _NodeType.CC_Node),
            self._Node((1, -1, -1), _NodeColor.Node_Green, _NodeType.CC_Node),
            self._Node((-1, 1, 1), _NodeColor.Node_Green, _NodeType.CC_Node),
            self._Node((-1, 1, -1), _NodeColor.Node_Green, _NodeType.CC_Node),
            self._Node((-1, -1, 1), _NodeColor.Node_Green, _NodeType.CC_Node),
            self._Node((-1, -1, -1), _NodeColor.Node_Green, _NodeType.CC_Node),

            # Blue nodes
            self._Node((-1, 1, 0), _NodeColor.Node_Blue, _NodeType.CC_Node),
            self._Node((-1, 0, 1), _NodeColor.Node_Blue, _NodeType.CC_Node),
            self._Node((-1, 0, -1), _NodeColor.Node_Blue, _NodeType.CC_Node),
            self._Node((-1, -1, 0), _NodeColor.Node_Blue, _NodeType.CC_Node),

            self._Node((0, 1, 1), _NodeColor.Node_Blue, _NodeType.CC_Node),
            self._Node((0, 1, -1), _NodeColor.Node_Blue, _NodeType.CC_Node),
            self._Node((0, -1, 1), _NodeColor.Node_Blue, _NodeType.CC_Node),
            self._Node((0, -1, -1), _NodeColor.Node_Blue, _NodeType.CC_Node),

            self._Node((1, 1, 0), _NodeColor.Node_Blue, _NodeType.CC_Node),
            self._Node((1, 0, 1), _NodeColor.Node_Blue, _NodeType.CC_Node),
            self._Node((1, 0, -1), _NodeColor.Node_Blue, _NodeType.CC_Node),
            self._Node((1, -1, 0), _NodeColor.Node_Blue, _NodeType.CC_Node),

            # Yellow nodes
            self._Node((1, 0, 0), _NodeColor.Node_Yellow, _NodeType.CC_Node),
            self._Node((-1, 0, 0), _NodeColor.Node_Yellow, _NodeType.CC_Node),
            self._Node((0, 1, 0), _NodeColor.Node_Yellow, _NodeType.CC_Node),
            self._Node((0, -1, 0), _NodeColor.Node_Yellow, _NodeType.CC_Node),
            self._Node((0, 0, 1), _NodeColor.Node_Yellow, _NodeType.CC_Node),
            self._Node((0, 0, -1), _NodeColor.Node_Yellow, _NodeType.CC_Node),
        ]

        self.max_depth = max_depth
        self.tree_type = tree_type

    def find_closest_node(self, point, level=-1):
        dot = lambda x, y: abs((x[0]-y[0])*(x[0] - y[0]) + (x[1]-y[1])*(x[1] - y[1]) + (x[2]-y[2])*(x[2]-y[2]))
        node = min([(dot(point, n.position), n) for n in self.roots], key=lambda x: x[0])[1]
        return node.find_closest_node(point)

    def expand_to(self, point):
        dot = lambda x, y: abs((x[0]-y[0])*(x[0] - y[0]) + (x[1]-y[1])*(x[1] - y[1]) + (x[2]-y[2])*(x[2]-y[2]))
        node = min([(dot(point, n.position), n) for n in self.roots], key=lambda x: x[0])[1]
        node.expand_to(point, 0, self.max_depth)
