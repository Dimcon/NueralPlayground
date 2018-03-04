from ANNObjects.ANNNode import ANNNode

class OutputNode(ANNNode):

	def __init__(self):
		self.value = 0.5
		self.output = ""

	def setoutout(self,output):
		self.output = output

	def setInput(self, inputs):
		self.value = inputs

	def Process(self):
		pass
