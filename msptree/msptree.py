"""
"""
class MSPTreeType:
	"""
	"""
	FunctionSpace, SpacePartitioning = range(2)


class MSPTree(object):
	"""
	"""
	class _NodeType:
    	CC_Node, BCC_Node, FCC_Node = range(3)

    class _NodeColor:
    	Node_Red, Node_Green, Node_Blue, Node_Yellow, Node_Ghost = range(5)

	class _Node:
		def __init__(self, position, color,  value = None):
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

