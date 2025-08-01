import numpy
import math

class Layer():

    def __init__(self):

        self.nodes = []


    def compute(self, inputs, weights, bias):

        output = 0

        if (len(inputs) == len(weights)):

            for i in range(len(inputs)):

                output += inputs[i] * weights[i]

            output += bias

            return output
        
        else:

            return "Error, inputs length isn't the same as weights length"


    def activation(self, x):

        output = 1.3 * math.tanh(x)
        return output


    def create(self, size, previous_size, previous_outputs, previous_weights, biases):

        self.size = size
        self.node = []

        for i in range(self.size):

            self.nodes.append([])

        for i in range(self.size):

            self.nodes[i] = [previous_outputs, previous_weights, biases[i], Layer().compute(previous_outputs, previous_weights, biases[i])]
        
        print(self.nodes)



#Layer(5).create() exemple de création de layer
ps = 2
po = [1, 2, 3]
pw = [2, 3, 4]
b = [1, 3, 5]
Layer().create(3, ps, po, pw, b)