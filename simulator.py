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
		self.sensor_input = range(parameters.number_sensors)
		self.firing_rates = range(parameters.number_neurons)

	# Generate network
	def generate_network(self):
		for i in range(parameters.number_neurons):
			self.neurons.append(neuron.Neuron())

		for i in self.sensor_input:
			self.sensor_input[i] = 0

		for i in self.firing_rates:
			self.firing_rates[i] = 0

	# Poisson gen
	def gen_poisson(self,rate):
		
		number = (parameters.max_time*rate)
		spike_list = numpy.add.accumulate(numpy.random.exponential(1.0/rate, size=number)*1/parameters.timestep)
		
		for i,item in enumerate(spike_list):
			spike_list[i] = int(spike_list[i])
		return spike_list

	# Update firing rates of neurons
	def update_firing_rates(self):

		for k,n in enumerate(self.neurons):

			self.firing_rates[k] = self.calc_firing_rate(n.spikes)

	def calc_firing_rate(self, spikes):

		if (spikes == []):
			return 0
		else:
			last_spike = spikes[-1]
			last_spikes = []
			inter_spike_intervals = []
			for s in spikes:
				if ((last_spike - s) < parameters.robot_update):
					last_spikes.append(s)
			for i in range(1,len(spikes)):
				inter_spike_intervals.append(spikes[i]-spikes[i-1])

			return 1/numpy.mean(inter_spike_intervals)

	# Simulate the network
	def sim_network(self,currents,spikes_in):

		# Simulation
		time_array = numpy.arange(0,parameters.max_time,parameters.timestep)

		for j in time_array:
			self.sim_network_step(currents,spikes_in)

	# Simulate the network for one timestep only
	def sim_network_step(self,currents,spikes_in):

		# Did the sensors emit spikes ?
		sensors_spikes = []
		for s in self.sensor_input:
			if (numpy.random.uniform(0,1) < s):
				sensors_spikes.append(1)
			else:
				sensors_spikes.append(0)

		# Update network
		for k,n in enumerate(self.neurons):

			# Connection from sensors
			sensor_connections = self.network[k][2]
			for c,connection in enumerate(sensor_connections):
				if (connection > 0 and sensors_spikes[c] == 1):
					self.neurons[k].spike_sensor_in = "Excitatory"

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