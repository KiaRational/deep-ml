import numpy as np

def divide_on_feature(X, feature_i, threshold):
    # Your code here

    split1 = X[X[:,feature_i]>=threshold]
    split2 = X[X[:,feature_i]<threshold]
    return [split1,split2]