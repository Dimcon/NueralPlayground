
class ANNNode:
	def __init__(self):
		self.prevnodes = []
		self.nextnodes = []
		self.value = 0.5
		self.influence = 0.5
		self.prevweights = []
		pass

	def setinluence(self, influence):
		self.influence = influence

	def resetNodes(self):
		self.prevnodes.clear()
		self.nextnodes.clear()

	def addPrevNode(self, node):
		self.prevnodes.append(node)

	def addNextNode(self, node):
		self.nextnodes.append(node)

	def setPrevNodes(self,prevnodes):
		self.prevnodes = prevnodes

	def setNextNodes(self,nextnodes):
		self.nextnodes = nextnodes