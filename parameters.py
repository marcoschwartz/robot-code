# Global parameters for neural network
number_neurons = 12
number_sensors = 4
neuron_type = "LIF"
neuron_dna_length = 1 + number_neurons + number_sensors
total_dna_length = neuron_dna_length*number_neurons

# Constants for evolution
mutation_rate = 0.1
population_size = 10
target = 1

# Constants for neural network
timestep = 1e-3
robot_update = 100e-3
robot_update_steps = int(robot_update/timestep)
max_time = 0.5
max_firing_rate = 1000.

# Robot parameters
max_distance = 260.