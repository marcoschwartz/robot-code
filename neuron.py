# AdEx simulator

# Imports
import numpy
import math
import parameters

# Main class
class Neuron:

	def __init__(self):
			
		if (parameters.neuron_type == "AdEx"):
			self.parameters = {"EL" : -58.0,	
				"gL" : 10.0,
				"Vt" : 0.0,
				"Vreset" : -58.0,
				"C" : 200.0,
				"a" : 0.0,
				"tw" : 300.0,
				"b" : 0.0,
				"dT" : 2.0,
				"Vexp" : -50.0, 
				"expAct" : 1.0,
				"gsynmax" : 4.0,
				"tausyn" : 10.0,
				"Esyn" : 0.0,
				"tref" : 1.0}

		if (parameters.neuron_type == "LIF"):
			self.parameters = {"EL" : -58.0,	
				"gL" : 10.0,
				"Vt" : -50.0,
				"Vreset" : -58.0,
				"C" : 200.0,
				"gsynmax" : 2.0,
				"tausyn" : 10.0,
				"Esyn" : 0.0,
				"tref" : 1.0}
			
		self.v = self.parameters['EL']*1e-3
		self.w = 0
		self.gsyn = 0
		self.ref_count = 0
		self.spikes = []
		
		self.record = True
		self.v_record = []
		self.multi_record = []
		self.time_count = 0
		self.gsyn_record = []
		self.spike_flag_out = False
		self.spike_flag_in = "None"
		self.spike_sensor_in = "None"

	def sim(self,stim,spikes_list=[],vp=[],vn=[],gp=[],gn=[]):
		
			# Increment time_count
			self.time_count = self.time_count + parameters.timestep
		
			# In refractory mode ?

			if (self.ref_count > 0):
				self.ref_count = self.ref_count - parameters.timestep

				if (self.spike_flag_in == "Excitatory"):
					self.spike_flag_in = "None"

				if (self.spike_flag_in == "Inhibitory"):
					self.spike_flag_in = "None"

			else:

				# Calculate spike input
				if (int(self.time_count/parameters.timestep) in spikes_list):
					# print 'spike_received from direct input a time t', self.time_count
					self.gsyn = self.gsyn + self.parameters['gsynmax']*1e-9

				if (self.spike_sensor_in == "Excitatory"):
					self.spike_sensor_in = "None"
					self.gsyn = self.gsyn + self.parameters['gsynmax']*1e-9

				if (self.spike_flag_in == "Excitatory"):
					self.spike_flag_in = "None"
					self.gsyn = self.gsyn + self.parameters['gsynmax']*1e-9

				if (self.spike_flag_in == "Inhibitory"):
					self.spike_flag_in = "None"
					self.gsyn = self.gsyn - self.parameters['gsynmax']*1e-9	
				
				self.gsyn = self.gsyn - self.gsyn * parameters.timestep / (self.parameters['tausyn']*1e-3)
				
				# Calculate contribution of other compartments
				multi_comp_contribution = 0
				
				if (vp != []):
					for i,item in enumerate(vp):
						multi_comp_contribution = multi_comp_contribution + gp[i]*1e-9*(vp[i] - self.v)/(self.parameters['C']*1e-12)
						
				if (vn != []):
					for i,item in enumerate(vn):
						multi_comp_contribution = multi_comp_contribution + gn[i]*1e-9*(vn[i] - self.v)/(self.parameters['C']*1e-12)
				
				if (parameters.neuron_type == "AdEx"):

					self.v = self.v + (-self.gsyn*(self.v-self.parameters['Esyn']*1e-3)/(self.parameters['C']*1e-12) + multi_comp_contribution - self.parameters['gL']*1e-9/(self.parameters['C']*1e-12) * (self.v-self.parameters['EL']*1e-3) + self.parameters['expAct']*self.parameters['gL']*1e-9*self.parameters['dT']*1e-3*math.exp((self.v-self.parameters['Vexp']*1e-3)/(self.parameters['dT']*1e-3))/(self.parameters['C']*1e-12) + stim/(self.parameters['C']*1e-12) - self.w/(self.parameters['C']*1e-12))*parameters.timestep
					self.w = self.w + (self.parameters['a']*1e-9*(self.v-self.parameters['EL']*1e-3) - self.w)/(self.parameters['tw']*1e-3)*parameters.timestep
				
				if (parameters.neuron_type == "LIF"):

					self.v = self.v + (-self.gsyn*(self.v-self.parameters['Esyn']*1e-3)/(self.parameters['C']*1e-12) + multi_comp_contribution - self.parameters['gL']*1e-9/(self.parameters['C']*1e-12) * (self.v-self.parameters['EL']*1e-3) + stim/(self.parameters['C']*1e-12))*parameters.timestep
					
				if (self.v > self.parameters['Vt']*1e-3):
					self.v = self.parameters['Vreset']*1e-3
					if (parameters.neuron_type == "AdEx"):
						self.w = self.w + self.parameters['b']*1e-9
					self.spikes.append(self.time_count)
					self.spike_flag_out = True
					self.ref_count = self.parameters['tref']*1e-3
			   
			if (self.record == True):
				self.v_record.append(self.v)
				#self.multi_record.append(multi_comp_contribution)
				self.gsyn_record.append(self.gsyn)
				
	def reset(self):
		
		self.v = self.parameters['EL']*1e-3
		self.w = 0
		self.gsyn = 0
		self.spikes = []
		
		self.v_record = []
		self.multi_record = []
		self.time_count = 0
		self.gsyn_record = []
