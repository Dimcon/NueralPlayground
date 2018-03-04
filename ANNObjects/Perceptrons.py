from ANNObjects.ANNNode import ANNNode


class Perceptron(ANNNode):

	def __init__(self):
		self.value = 0.5

	def setInput(self,inputs):
		self.value = inputs

	def Process(self):
		pass



