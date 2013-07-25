# Converter DNA to neural network
import parameters

class DnaNeuralNetwork():

	def __init__(self):
		pass

	# Create network from DNA (list of neurons with type, targets, and inputs)
	def dna_to_neural_network(self,dna):
		neurons = []
		for i in range(parameters.number_neurons):
			neuron = []
			dna_chunk = dna[i*parameters.neuron_dna_length:(i+1)*parameters.neuron_dna_length]

			# Neuron type
			if (dna_chunk[0] == 0):
				neuron.append("Excitatory")
			else:
				neuron.append("Inhibitory");

			# Neuron targets
			neuron.append(dna_chunk[1:1+parameters.number_neurons])

			# Neuron inputs
			neuron.append(dna_chunk[1+parameters.number_neurons:1+parameters.number_neurons+parameters.number_sensors])

			# Add to neurons
			neurons.append(neuron)

		return neurons 