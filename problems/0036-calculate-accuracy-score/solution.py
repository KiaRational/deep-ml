import numpy as np

def accuracy_score(y_true, y_pred):
	
    return np.sum(np.where(y_true == y_pred , 1 , 0 ))/y_pred.shape[0]