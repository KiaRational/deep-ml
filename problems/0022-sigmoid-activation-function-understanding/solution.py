import math
import numpy as np
def sigmoid(z: float) -> float:
	#Your code here
	if z!=0:
		result = 1 / (1 + math.exp(-1*z))
	else:
		result = 0.5
		
	return np.round(result,4)