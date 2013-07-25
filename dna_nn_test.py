# Imports
import dna_nn
import parameters
from random import randrange, uniform

# Neuron parameters (fixed in first version)

# Generate test DNA
dna = []
for n in range(parameters.number_neurons):

	# Exc/Inh
	dna.append(randrange(0, 2))

	# Connections to other neurons
	for n in range(parameters.number_neurons):
		dna.append(randrange(0, 2))

	# Connection from sensors
	for n in range(parameters.number_sensors):
		dna.append(randrange(0, 2))

# Convert to neural network
dna_nn = dna_nn.DnaNeuralNetwork()
neurons = dna_nn.dna_to_neural_network(dna)

for n in neurons:
	print n