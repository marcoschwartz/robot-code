# Imports
import numpy as np
import pylab
import parameters
import evolution
import sys

# Variables for evolution
nb_generations = 1000
max_fitness = []

# Evolution module
evo = evolution.Evolution()

# Create initial population
pool = evo.gen_init_population()

# Main loop
for i in range(nb_generations):

	# Select best individuals
	mating_pool, best_fitness = evo.selection(pool)
	max_fitness.append(best_fitness)

	# Crossover
	crossover_pool = evo.crossover(mating_pool)

	# Mutation
	mutated_pool = evo.mutate(crossover_pool)

	# Evaluate fitness of pool
	pool = evo.calc_fitness_pool(mutated_pool)

	# Over ?
	if (max_fitness[-1] < 1e-3):
		break

# Best individual
best_fitness, best_individual, best_index = evo.find_best_fitness(pool)
print "Best individual :", best_individual, "with fitness", best_fitness

# Plot
evo.plot_fitness(max_fitness)


