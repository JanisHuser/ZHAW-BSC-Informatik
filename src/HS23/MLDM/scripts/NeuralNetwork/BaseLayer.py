import random
class BaseLayer():
	
	def __init__(self, node_count, activation_function=None, weights=None, biases=None):
		self._node_count = node_count
		self._activation_function = activation_function
		self._weights = weights
		self._biases = biases
		self._next_node_count = 0
		self._weight_count = 0
		self._nets = []
		self._inputs = []
		self._outs = []
		
	def _initialize_weights(self, weight_count):
		if self._weights is not None:
			return
		
		self._weights = [random.uniform(0, 1) for _ in range(weight_count)]


	def _initialize_biases(self, biases_count):
		if self._weights is not None:
			return
		
		self._biases = [random.uniform(0, 1) for _ in range(biases_count)]

	def initialize(self, next_node_count):
		self._next_node_count = next_node_count
		self._weight_count = next_node_count * self._node_count
		self._initialize_weights(self._weight_count)
		self._initialize_biases(self._node_count)

	def forward_pass(self, input):

		self._input = input
		values = []

		wi = 0
		while self._weight_count > wi:
			sum = 0
			for in_val in input:
				sum += (in_val * self._weights[wi])
				wi += 1


			values.append(sum)
		return values
	
	def get_input_for_weights(self, input):
		values = []

		wi = 0
		while self._weight_count > wi:
			for in_val in input:
				values.append(in_val)
		return values
	
	def set_nets(self, nets):
		self._nets = nets

	def set_outs(self, outs):
		self._outs = outs