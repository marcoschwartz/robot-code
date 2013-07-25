# Imports
import simulator
import numpy
import time
import parameters
import sys

# Parameters
rate = 45

# Network description
network = [['Excitatory', [1, 1, 0, 1, 1, 0, 1, 1, 0, 1], [0, 1]],
['Excitatory', [0, 0, 1, 1, 1, 0, 1, 0, 1, 0], [1, 0]],
['Inhibitory', [1, 0, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1]],
['Excitatory', [1, 0, 0, 1, 1, 0, 1, 1, 0, 0], [1, 0]],
['Inhibitory', [0, 0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1]],
['Inhibitory', [1, 0, 1, 1, 0, 1, 0, 0, 0, 1], [1, 1]],
['Excitatory', [0, 1, 1, 0, 0, 1, 1, 1, 1, 0], [1, 0]],
['Excitatory', [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], [1, 1]],
['Excitatory', [1, 0, 1, 0, 1, 1, 1, 0, 1, 0], [1, 0]],
['Inhibitory', [1, 1, 0, 0, 0, 1, 1, 0, 0, 1], [0, 1]]]

# Create simulator
sim = simulator.Simulator(network)

currents = []
spikes_in = []
for i in range(parameters.number_neurons):
	
	# Currents for each neurons
	currents.append(0)

	# Spike input for each neuron
	spikes_in.append([])

spikes_in[0] = sim.gen_poisson(rate,5)

# Calculate network
sim.generate_network()

start_sim = time.time()
sim.sim_network(currents,spikes_in)
print "Time to simulate:", time.time() - start_sim
print "Acceleration factor:", parameters.max_time/(time.time() - start_sim)

# Plot result
sim.plot_spikes()