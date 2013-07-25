import parameters
import math

# Interface between the robot and the neural network
class RobotInterface():

	# Init
	def __init__(self):
		pass

	# Convert firing rate to motor command
	def rate_to_motor(self, rate_forward, rate_backward):

		# Sum both rates
		sum_rate = rate_forward - rate_backward

		# Determine direction
		if (sum_rate < 0):
			direction = 0
		else:
			direction = 1

		# Determine speed
		speed = math.fabs(sum_rate)/parameters.max_firing_rate*255

		return speed, direction

	# Convert ultrasonic data to spikes
	def ultrasonic_to_probability(self, sensor_data):

		return sensor_data/parameters.max_distance


