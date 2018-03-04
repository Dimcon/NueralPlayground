from ANNObjects.ANNNode import ANNNode
from ANNObjects.InputNode import InputNode
from ANNObjects.Perceptrons import Perceptron
from ANNObjects.OutputNode import OutputNode


class Processor():
	def __init__(self):
		self.FirstNode = InputNode()
		self.degree = 2
		self.dimensions = [0, 0]
		self.layers = []
		self.layers.append(self.FirstNode)
		self.defaultweight = 0.5
		self.defaultinfluence = 0.5
		self.valuelimit = 255
		self.result = -1

	def setInputs(self, inputs, dimensions, valuelimit):
		self.degree = len(dimensions)
		self.FirstNode.setInputs(inputs)
		self.valuelimit = valuelimit

	def doitall(self, inputs, dimensions, valuelimit,outputs):
		self.setInputs(inputs, dimensions, valuelimit)
		self.createNetwork()
		self.addLayer(ANNNode, 800)
		self.addLayer(ANNNode, 1600)
		self.addLayer(ANNNode, 100)
		self.addLayer(ANNNode, 50)
		self.addLayer(ANNNode, 20)
		self.addLayer(ANNNode, 10)
		self.addOutputs(outputs)

	def createNetwork(self):
		perceptroncount = len(self.FirstNode.values)
		layer1 = []
		for i in range(perceptroncount):
			p = Perceptron()
			p.prevweights = [1]
			p.influence = 1
			layer1.append(p)
		self.layers.append(layer1)
		self.FirstNode.nextnodes = layer1

	def addLayer(self, NodeType, count):
		layer = []
		for i in range(count):
			n = NodeType()
			n.prevnodes = self.layers[len(self.layers) - 1]
			layer.append(n)
		for node in self.layers[len(self.layers) - 1]:
			node.nextnodes = layer
		prevcount = len(self.layers[len(self.layers)-1])
		weights = []
		for i in range(prevcount):
			weights.append(self.defaultweight)
		for node in layer:
			node.prevweights = weights
			node.influence = self.defaultinfluence
		self.layers.append(layer)

	def addOutputs(self, outputs):
		layer = []
		for i in range(len(outputs)):
			n = OutputNode()
			n.setoutout(outputs[i])
			n.prevnodes = self.layers[len(self.layers) - 1]
			layer.append(n)
		for node in self.layers[len(self.layers) - 1]:
			node.nextnodes = layer
		prevcount = len(self.layers[len(self.layers)-1])
		weights = []
		weights2 = []
		for i in range(prevcount):
				weights.append(self.defaultweight)
		for i in range(prevcount):
			weights2.append(0.9)

		for i in range(len(layer)):
			node = layer[i]
			if i < 5: node.prevweights = weights
			else: node.prevweights = weights2
			node.influence = self.defaultinfluence
		self.layers.append(layer)

	def Process(self):
		layers = self.layers
		prevavg = 0
		for i in range(len(layers)):
			print("Processing layer: {}".format(i))
			layer = layers[i]
			if i == 0:
				print("Passing first layer".format())
				pass
			elif i == 1:
				print("Handling Perceptron layer {}".format(i))
				for j in range(len(layer)):
					node = layer[j]
					node.value = float(self.FirstNode.values[j]) / float(self.valuelimit)
			else:
				print("Processing hidden layer {}".format(i))
				oldlayer = self.layers[i - 1]
				newlayer = layer
				for nnode in newlayer:
					weights = nnode.prevweights
					avg = 0
					for n in range(len(oldlayer)):
						temp = 0
						value = oldlayer[n].value * weights[n]
						avg += value + temp
					avg = avg / len(oldlayer)
					nnode.value = avg
				if i == len(layers) - 1:
					print("Handling Final layer {}".format(i))
					oldlayer = self.layers[i - 1]
					maxconfidence = 0
					result = -1
					for nnode in layer:
						if nnode.value > maxconfidence:
							maxconfidence = nnode.value
							result = nnode.output
					self.result = result
					print("Result = {}".format(result))
					return result
