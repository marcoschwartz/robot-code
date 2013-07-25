# Imports
import numpy as np
import pylab
import parameters

class Evolution():

	def __init__(self):
		pass

	def calc_fitness_individual(self,individual):
		fitness = 0.
		sum_elements = 0.
		for i in individual:
			sum_elements = sum_elements + i
		fitness = (sum_elements - parameters.target)*(sum_elements - parameters.target)

		return fitness

	def calc_fitness_pool(self,pool):
		for i in pool:
			i[1] = self.calc_fitness_individual(i[0])

		return pool

	def gen_individual(self):
		individual = []
		for i in range(parameters.total_dna_length):
			individual.append(np.random.uniform(0,1))
		return individual

	def gen_init_population(self):
		pool = []

		for i in range(parameters.population_size):
			individual = self.gen_individual()
			individual_fitness = self.calc_fitness_individual(individual)
			pool.append([individual,individual_fitness])

		return pool
		
	def selection(self, pool):

		mating_pool = []

		# Find best fitness
		first_fitness, first_individual, best_index = self.find_best_fitness(pool)
		max_fitness = first_fitness

		# Remove best element
		pool.pop(best_index)

		# Find best fitness
		second_fitness, second_individual, best_index = self.find_best_fitness(pool)

		mating_pool.append(first_individual)
		mating_pool.append(second_individual)

		return mating_pool, max_fitness

	def find_best_fitness(self, pool):
		best_fitness = pool[0][1]
		best_individual = pool[0][0]
		best_index = 0
		for i,item in enumerate(pool):
			if (best_fitness > item[1]):
				best_fitness = item[1]
				best_individual = item[0]
				best_index = i
		return best_fitness, best_individual, best_index

	def crossover(self,mating_pool):

		crossover_pool = []

		for i in range(parameters.population_size):
			individual = self.crossover_individual(mating_pool)
			individual_fitness = 0
			crossover_pool.append([individual,individual_fitness])
		return crossover_pool

	def crossover_individual(self,mating_pool):
		child = []
		for i in range(parameters.total_dna_length):
			# Select parent A or B
			if (np.random.uniform(0,1) > 0.5):
				child.append(mating_pool[0][0])
			else:
				child.append(mating_pool[1][0])
		return child

	def mutate(self, pool):
		for i in pool:
			for j in range(parameters.total_dna_length):
				if (np.random.uniform(0,1) < parameters.mutation_rate):
					i[0][j] = i[0][j]*np.random.uniform(0,1)
		return pool

	def plot_fitness(self,max_fitness):
		pylab.plot(range(len(max_fitness)),max_fitness)
		pylab.show()