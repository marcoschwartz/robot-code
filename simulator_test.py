# Imports
import simulator
import numpy
import time
import parameters
import sys

# Parameters
rate = 10

# Network description
network = [['Excitatory', [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0]],
['Excitatory', [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0]],
['Excitatory', [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 1, 0]],
['Excitatory', [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1]],

['Excitatory', [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0]],
['Excitatory', [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0]],
['Excitatory', [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0]],
['Excitatory', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0]],

['Excitatory', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0]],
['Excitatory', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0]],
['Excitatory', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0]],
['Excitatory', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0]]]

# Create simulator
sim = simulator.Simulator(network)

currents = []
spikes_in = []
for i in range(parameters.number_neurons):
	
	# Currents for each neurons
	currents.append(0)

	# Spike input for each neuron
	spikes_in.append([])

#spikes_in[0] = sim.gen_poisson(rate)

# Generate network
sim.generate_network()

# Simulate
start_sim = time.time()

sim.sensor_input = [0.1,0.2,0.3,0.4]
robot_timer = 0

for j in numpy.arange(0,parameters.max_time,parameters.timestep):

	# Update network
	sim.sim_network_step(currents,spikes_in)

	# Update firing rates and sensors input
	robot_timer = robot_timer + 1
	if (robot_timer == parameters.robot_update_steps):
		robot_timer = 0
		sim.update_firing_rates()
		sim.sensor_input = [0.1,0.2,0.3,0.4]

print "Time to simulate:", time.time() - start_sim
print "Acceleration factor:", parameters.max_time/(time.time() - start_sim)

# Plot result
sim.plot_spikes()