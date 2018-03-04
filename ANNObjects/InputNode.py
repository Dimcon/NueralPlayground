from ANNObjects.ANNNode import ANNNode


class InputNode(ANNNode):

	def __init__(self):
		self.values = []

	def setInputs(self,inputs):
		self.values = inputs

	def addInput(self,input):
		self.values.append(input)

	def Process(self):
		pass



