
class base():

	def __init__(self, equation: str):
		self._equation = equation

	"""
	"""
	def max_iterations(self, error):
		raise NotImplementedError("max iterations is not implemented")