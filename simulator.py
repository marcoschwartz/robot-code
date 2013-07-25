import neuron
import numpy
import time
import parameters
import sys
from matplotlib.pylab import *

class Simulator:

	# Init
	def __init__(self,network):
		self.network = network
		self.neurons = []

	# Generate network
	def generate_network(self):
		for i in range(parameters.number_neurons):
			self.neurons.append(neuron.Neuron())

	# Poisson gen
	def gen_poisson(self,rate,seed):
		
		number = (parameters.max_time*rate)
		numpy.random.seed(seed)
		spike_list = numpy.add.accumulate(numpy.random.exponential(1.0/rate, size=number)*1/parameters.timestep)
		
		for i,item in enumerate(spike_list):
			spike_list[i] = int(spike_list[i])
		return spike_list

	# Simulate the network
	def sim_network(self,currents,spikes_in):

		# Simulation
		time_array = numpy.arange(0,parameters.max_time,parameters.timestep)

		for j in time_array:
			self.sim_network_step(currents,spikes_in)

	def sim_network_step(self,currents,spikes_in):
		for k,n in enumerate(self.neurons):
			n.sim(currents[k],spikes_in[k])
				
			# Reset output flags
			if (n.spike_flag_out == True):
				n.spike_flag_out = False
				
				# Signal spikes to target neurons
				targets = self.network[k][1]
				for target,weight in enumerate(targets):
					if (weight > 0):
						self.neurons[target].spike_flag_in = self.network[k][0]

	# Plot all voltage traces
	def plot_voltages(self):
		# Plot
		time_array = numpy.arange(0,parameters.max_time,parameters.timestep)
		for i in self.neurons:
			plot(time_array,i.v_record)

		show()

	# Plot all spike traces
	def plot_spikes(self):
		# Plot
		for n,neuron in enumerate(self.neurons):
			for t in neuron.spikes:
				plot([t,t],[2*n,2*n+1],c="k",linewidth=1)

		show()