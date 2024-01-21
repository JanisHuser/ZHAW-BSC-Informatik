from .BaseLayer import BaseLayer

class OutputLayer(BaseLayer):
	
	def propagate_back(self, y):

		node_count = self._node_count

		outs_output = self._outs[-node_count:]

		e_total = self.calc_mse(outs_output, y)

		e_total__outs_output = [-y[i] - self._outs[i] for i in range(node_count)] 

		outs_output__nets_output = [self._activate_partial(x, self._layers[-1]) for x in outs_output]

		nets_output__weights_output = self._layers[-1].get_input_for_weights(outs_output)

		target_for_weight =  self._layers[-1].get_input_for_weights(y)


		
		