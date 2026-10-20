import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	grad = 1
	for i in range(len(functions) -1, -1, -1):
		if functions[i]=='square':
			deriv=2*x
			x=x**2
		elif functions[i]=='sin':
			deriv=np.cos(x)
			x = np.sin(x)
		elif functions[i]=='exp':
			deriv = np.exp(x)
			x = np.exp(x)

		elif functions[i]=='log':
			deriv = 1/x
			x = np.log(x)
		grad*=deriv

	return grad